import os
import io
import time
import threading
import onnxruntime as ort
from PIL import Image, ImageFile
from queue import Queue, Empty
from flask import Flask, request, render_template, send_file, jsonify
from rembg.bg import remove

app = Flask(__name__, template_folder='./templates/')

ImageFile.LOAD_TRUNCATED_IMAGES = True
requests_queue = Queue()
BATCH_SIZE = 1
CHECK_INTERVAL = 0.1
u2net_path = os.environ['U2NET_HOME'] + '/u2net.onnx'
ort_session = ort.InferenceSession(u2net_path, providers=ort.get_available_providers())


def handle_requests_by_batch():
    while True:
        requests_batch = []
        while not (len(requests_batch) >= BATCH_SIZE):
            try:
                requests_batch.append(requests_queue.get(timeout=CHECK_INTERVAL))
            except Empty:
                continue

            for request in requests_batch:
                org_img_bytes, bg_img_bytes = request['input']
                request['output'] = run(org_img_bytes, bg_img_bytes)

threading.Thread(target=handle_requests_by_batch).start()


def run(org_img_bytes, bg_img_bytes):
    try:
        mask = remove(org_img_bytes, session=ort_session, only_mask=True)
        mask = Image.open(io.BytesIO(mask))

        org_img = Image.open(io.BytesIO(org_img_bytes)).convert("RGB")
        bg_img = Image.open(io.BytesIO(bg_img_bytes)).convert("RGB")
        bg_img = bg_img.resize(org_img.size, Image.LANCZOS)

        result = Image.composite(org_img, bg_img, mask)

        bio = io.BytesIO()
        result.save(bio, "PNG")
        bio.seek(0)

        return bio
    except Exception as e:
        return jsonify({'error': 'Exception occurs while changing background'}), 500


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/change-bg", methods=["POST"])
def change_bg():
    if requests_queue.qsize() > BATCH_SIZE:
        return jsonify({'error': 'Too Many Reqeusts'}), 429

    org_img_bytes = request.files['orgImage'].read()
    bg_img_bytes = request.files['bgImage'].read()

    req = {
        'input': [org_img_bytes, bg_img_bytes]
    }

    requests_queue.put(req)

    while 'output' not in req:
        time.sleep(CHECK_INTERVAL)

    io = req['output']
    if io == "error":
        return jsonify({'error': 'Server error'}), 500

    return send_file(io, mimetype="image/png")


@app.route("/healthz", methods=["GET"])
def check_health():
    return "healthy", 200


if __name__ == "__main__":
    from waitress import serve
    serve(app, host='0.0.0.0', port=80)
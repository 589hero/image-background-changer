FROM 589hero/u2net-onnx:latest

COPY . /app
WORKDIR /app
 
RUN pip install -r requirements.txt

CMD ["python", "server.py"]
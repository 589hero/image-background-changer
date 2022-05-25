[![Run on Ainize](https://ainize.ai/images/run_on_ainize_button.svg)](https://ainize.web.app/redirect?git_repo=https://github.com/589hero/image-background-changer-demo)

# Image Background Changer Demo
You can change background of images on this <a href="https://main-image-background-changer-589hero.endpoint.ainize.ai/">webpage</a>.

Just upload Original Image and Background Image and Press "Run" button!

## Examples
<table>
    <thead>
        <tr>
            <td>Original Image</td>
            <td>Background Image</td>
            <td>Result Image</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><img src="https://github.com/589hero/image-background-changer-demo/blob/main/static/images/animal-1.jpg?raw=true" width="300" height="200"/></td>
            <td><img src="https://github.com/589hero/image-background-changer-demo/blob/main/static/images/forest-1.jpeg?raw=true" width="300" height="200"/></td>
            <td><img src="https://github.com/589hero/image-background-changer-demo/blob/main/static/images/animal-1-out.png?raw=true" width="300" height="200"/></td>
        </tr>
        <tr>
            <td><img src="https://github.com/589hero/image-background-changer-demo/blob/main/static/images/car-1.jpg?raw=true" width="300" height="200"/></td>
            <td><img src="https://github.com/589hero/image-background-changer-demo/blob/main/static/images/sky-1.jpeg?raw=true" width="300" height="200"/></td>
            <td><img src="https://github.com/589hero/image-background-changer-demo/blob/main/static/images/car-1-out.png?raw=true" width="300" height="200"/></td>
        </tr>
    </tbody>
</table>


## Usage as a Docker
```
1. docker build -t <YOUR_OWN_IMAGE_NAME> .
2. docker run -it -p 80:80 <YOUR_OWN_IMAGE_NAME>
```
## Reference
- https://github.com/danielgatis/rembg
- https://github.com/Jeong-Hyun-Su/neural-style-tf
- https://github.com/woomurf/generative_inpainting

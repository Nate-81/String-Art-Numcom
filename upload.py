from flask import Flask, render_template, request, send_file
from PIL import Image, ImageDraw, ImageOps
from io import BytesIO

app = Flask('Image Uploader')


@app.route('/')
def index():
    return render_template('./index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    if file:
        image = Image.open(file)

        # Resize image to a square
        size = min(image.size)
        image = ImageOps.fit(image, (size, size), Image.ANTIALIAS)
        width, height = image.size

        # Create a circular mask
        mask = Image.new('L', image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, size, size), fill=255)

        # Apply circular mask to the image
        circular_image = Image.new('RGB', (width, height))
        circular_image.paste(image, mask=mask)

        # Save or serve the resulting image
        output = BytesIO()
        output_path = "/Users/nathans./Documents/NumCom/StringArt_Py/images/test.png"
        circular_image.save(output, format='PNG')
        circular_image.save(output_path, format='PNG')
        output.seek(0)
        return send_file(output, mimetype='image/png')


def run_app():
    app.run(debug=True)

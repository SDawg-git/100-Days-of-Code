from flask import Flask, render_template, url_for, request, redirect, session
from flask_bootstrap import Bootstrap5
from PIL import Image
import itertools

app = Flask(__name__)
app.config['SECRET_KEY'] = og.environ.get["SECRET_KEY"]
Bootstrap5(app)


@app.route("/", methods=["GET","POST"])
def home():

    sorted_hexcodes = {}

    if request.method == "POST":
        if "picture" not in request.files:
            return "No file part", 400

        picture = request.files["picture"]

        open_image = Image.open(picture)
        img = open_image.convert("RGB")
        width, height = img.size


        all_hexcodes = {}

        for x in range(0, width):                       #iterates through all pixels in image
            for y in range(0, height):
                r, g, b = img.getpixel((x, y))          #saves current pixel in RGB terms
                #print(img.getpixel((x, y)))
                pixel_hex = '#%02x%02x%02x' % img.getpixel((x, y))      #turns RGB into HEXCODE
                #print(pixel_hex)

                if pixel_hex not in all_hexcodes:
                    all_hexcodes[pixel_hex] = 1
                else:
                    all_hexcodes[pixel_hex] += 1
        sorted_hexcodes = dict(sorted(all_hexcodes.items(), key=lambda item: item[1], reverse=True))



        if len(sorted_hexcodes) > 10:
            sorted_hexcodes = dict(itertools.islice(sorted_hexcodes.items(), 10))

        for code in sorted_hexcodes:
            print(code)

        session["hexcodes"] = list(sorted_hexcodes.keys())

        return redirect(url_for("home"))

    hexcodes = session.get("hexcodes", [])
    return render_template("index.html", hexcodes = hexcodes)



if __name__ == '__main__':
    app.run(debug=True)

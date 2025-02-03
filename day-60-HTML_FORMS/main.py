from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def receive_data():
    if request.method == "POST":
            return f"<h1>{request.form['username']}, {request.form['password']}</h1>"

    return "Error"

if __name__ == "__main__":
    app.run(debug=True)


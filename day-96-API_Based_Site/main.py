from flask import Flask, jsonify, render_template, request
import requests
from flask_bootstrap import Bootstrap5


site_url = ("https://api.openbrewerydb.org/v1/")



app = Flask(__name__)
Bootstrap5(app)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/all-breweries")
def all_breweries():

    response = requests.get(url=f"{site_url}breweries")
    response.raise_for_status()
    data = response.json()

    return jsonify(data)


@app.route("/by_city", methods=["POST"])
def by_city():

    city_name = request.form.get("city_name")


    response = requests.get(url=f"{site_url}breweries?by_city={city_name}")
    response.raise_for_status()
    data = response.json()

    if not data:
        return jsonify({f"Not Found": f"No breweries found in {city_name}."})
    else:
        return jsonify(data)


@app.route("/by_name", methods=["POST"])
def by_name():

    brewery_name = request.form.get("brewery_name")


    response = requests.get(url=f"{site_url}breweries?by_name={brewery_name}")
    response.raise_for_status()
    data = response.json()

    if not data:
        return jsonify({f"Not Found": f"No breweries found under the name {brewery_name}."})
    else:
        return jsonify(data)


@app.route("/by_type", methods=["POST"])
def by_type():

    brewery_type = request.form.get("brewery_types")

    response = requests.get(url=f"{site_url}breweries?by_type={brewery_type}")
    response.raise_for_status()
    data = response.json()

    if not data:
        return jsonify({f"Not Found": f"No breweries found under the type {brewery_type}."})
    else:
        return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True)

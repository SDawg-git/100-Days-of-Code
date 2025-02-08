
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from select import select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random
from sqlalchemy import select



app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random", methods=["GET"])
def random_cafe():

    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)

    # cafe_names = []
    # for cafe in all_cafes:                    #no need to do this, issue was with naming the function "random", it was clashing with the import
    #     cafe_names.append(cafe.name)
    #random_cafe = random.choice(cafe_names)

    print(random_cafe)

    return render_template("index.html")


@app.route("/all", methods=["GET"])
def all_cafes():

    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    cafes_list = []
    for cafe in all_cafes:
        cafe_dict = {
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "has_sockets": cafe.has_sockets,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "can_take_calls": cafe.can_take_calls,
            "seats": cafe.seats,
            "coffee_price": cafe.coffee_price,
        }
        cafes_list.append(cafe_dict)

    return jsonify(cafes=cafes_list)


@app.route("/search", methods=["GET"])
def search_cafes():

    location = request.args.get("loc")
    #print(location)

    result = db.session.execute(db.select(Cafe).where(Cafe.location == location))
    near_cafes = result.scalars().all()

    if not near_cafes:
        return jsonify(error={"Not Found" : "No cafes at given location"})
    else:
        cafes_list = []
        for cafe in near_cafes:
            cafe_dict = {
                "id": cafe.id,
                "name": cafe.name,
                "map_url": cafe.map_url,
                "img_url": cafe.img_url,
                "location": cafe.location,
                "has_sockets": cafe.has_sockets,
                "has_toilet": cafe.has_toilet,
                "has_wifi": cafe.has_wifi,
                "can_take_calls": cafe.can_take_calls,
                "seats": cafe.seats,
                "coffee_price": cafe.coffee_price,
            }
            cafes_list.append(cafe_dict)
        return jsonify(cafes=cafes_list)

# HTTP GET - Read Record

# HTTP POST - Create Record

@app.route("/add", methods=["POST"])
def add_cafe():

    if request.method == "POST":
        #data = request.form
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("location"),
            has_sockets=bool(request.form.get("has_sockets")),
            has_toilet=bool(request.form.get("has_toilet")),
            has_wifi=bool(request.form.get("has_wifi")),
            can_take_calls=bool(request.form.get("can_take_calls")),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"),
        )
        db.session.add(new_cafe)
        db.session.commit()

        return jsonify(response={"success": "Successfully added the new cafe."})






# HTTP PUT/PATCH - Update Record


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):

    if request.method == "PATCH":
        new_price = request.args.get("new_price")
        #selected_cafe_id = request.args.get("cafe_id")

        chosen_cafe = db.get_or_404(Cafe, cafe_id)

        if chosen_cafe:
            chosen_cafe.coffee_price = new_price
            db.session.commit()

            return jsonify({"Success":"Successfully updated the price."})

        else:
            return jsonify({f"Not Found": f"No cafe found under the id of {cafe_id}."}), 404



# HTTP DELETE - Delete Record

TopSecretAPIKey = "12345"

@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def report_closed(cafe_id):

    sent_key = request.args.get("api-key")
    #cafe = db.get_or_404(Cafe, cafe_id)
    cafe = db.session.get(Cafe, cafe_id)   #had to change code to this, otherwise flask would overwrite the id not found error with its own



    if sent_key == TopSecretAPIKey:

        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify({"Success":"Cafe was successfully removed from the database."})

        else:
            return jsonify({f"Not Found": f"No cafe found under the id of {cafe_id}."}), 404
    else:
        return jsonify({"Error":"You do not have the correct API key."}), 403



if __name__ == '__main__':
    app.run(debug=True)

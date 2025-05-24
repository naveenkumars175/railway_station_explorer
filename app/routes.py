from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    stations = [
        {"name": "Chennai Central", "image": "station1.jpg", "location": "13.0827°N, 80.2707°E"},
        {"name": "Mumbai CST", "image": "station2.jpg", "location": "18.9402°N, 72.8356°E"}
    ]
    return render_template("index.html", stations=stations)


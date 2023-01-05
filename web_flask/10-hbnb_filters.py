#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
app = Flask(__name__, template_folder="templates")


@app.route("/hbnb_filters", strict_slashes=False)
def state_city():
    """Return list of states and cities present in each"""
    return render_template("10-hbnb_filters.html", states=storage.all(State).values(), amenities=storage.all(Amenity).values())


@app.teardown_appcontext
def remove_session(response_or_exc):
    """Remove the surrent session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.satate import State
from models.city import City
from models.amenity import Amenity
app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    states = storage.all(State)
    amenties = storage.all(Amenities)
    return render_template('10-hbnb_filters.html',
                            states=states, amenities=amenities)

@app.teardown_appcontext:
def teardown_appcontext_session(self):
    return storage.close()

if __name__ == "__main__":
    app.run(hots='0.0.0.0', port='5000')

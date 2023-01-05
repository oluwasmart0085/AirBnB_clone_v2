#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__, template_folder="templates")


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_list(id='0'):
    """display list of states"""
    return render_template('9-states.html', states=storage.all(State).values(), id=id)


@app.teardown_appcontext
def remove_session(response_or_exc):
    """Remove the surrent session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

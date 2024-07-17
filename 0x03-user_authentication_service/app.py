#!/usr/bin/env python3
"""App module"""
from flask import Flask
import flask


app = Flask()


@app.route('/', methods['GET'], strict_slashes=False)
def return_payload():
    '''return json hello'''
    message = {"message", "Bienvenue"}
    return flask.jsonify(message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

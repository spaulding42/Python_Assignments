from flask import Flask, render_template, request, redirect
from flask_app import app
from flask_app.controllers import login
from flask_app.controllers import sighting_controller



if __name__ == "__main__":
    app.run(debug=True)


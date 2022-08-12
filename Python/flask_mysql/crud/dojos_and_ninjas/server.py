from flask import Flask, render_template, request, redirect
from flask_app import app
from flask_app.controllers import ninjas_controller
from flask_app.controllers import dojos_controller

@app.route('/')
def goto_dojos():
    return redirect ('/dojos')

if __name__ == "__main__":
    app.run(debug=True)
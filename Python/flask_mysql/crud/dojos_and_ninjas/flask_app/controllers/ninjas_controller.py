from flask_app import app
from flask import Flask, render_template,redirect,request,session
from flask_app.controllers import dojos_controller
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

@app.route('/add_ninja')
def add_ninja():
    dojos = Dojo.get_all()
    return render_template("add_ninjas.html", dojos=dojos )

@app.route('/process_new_ninja', methods = ['POST'])
def process_ninja():
    Ninja.create(request.form)
    id = request.form['dojo_id']
    return redirect(f'/dojos/ninjas/{id}')


# Delete ACTION section for ninjas OR dojos
# @app.route('/delete/ninja/<int:id>')
# def delete_ninja(id):
#     pass

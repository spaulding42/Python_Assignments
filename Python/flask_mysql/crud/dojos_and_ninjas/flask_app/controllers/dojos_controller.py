from flask_app import app
from flask import Flask, render_template,redirect,request,session
# from flask_app.controllers import ninjas_controller
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

@app.route("/dojos")
def index():
    dojos = Dojo.get_all()
    return render_template("dojos.html", dojos = dojos)


@app.route("/add/dojo", methods = ['POST'])
def process_dojo():
    #make sure the form wasn't empty before making a new DB entry
    dojo_name = request.form['name']
    if dojo_name != '':
        Dojo.add_dojo(request.form)
    
    return redirect('/dojos')

@app.route('/dojos/ninjas/<int:id>')
def list_dojos_ninjas(id):
    data = {
        'id': id
    }
    ninjas_in_dojo = Dojo.list_one_dojo(data)
    return render_template("dojos_ninjas.html", ninjas_in_dojo = ninjas_in_dojo)

#not using this right now
@app.route('/delete/dojo/<int:id>')
def delete_dojo(id):
    pass

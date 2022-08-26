from flask_app import app
from flask import render_template,redirect,request,session,flash
# from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user_model import User
from flask_app.models.sighting_model import Sighting

@app.route('/welcome')
def welcome():
    if 'id' in session:
        data = {
            'id': session['id']
        }
        user = User.lookup_by_id(data)
        print(user.first_name)
        all_sightings = Sighting.get_all()
        return render_template("welcome.html", user = user, all_sightings = all_sightings)
    print("no session")
    return redirect('/')

#display route
@app.route('/sighting/edit/<int:id>')
def edit_sighting(id):
    if 'id' not in session:
        return redirect('/')
    sighting_to_edit = {
        'id': id
    }
    user_data = {
        'id': session['id']
    }
    user = User.lookup_by_id(user_data)
    sighting = Sighting.get_sighting_by_id(sighting_to_edit)
    if sighting.user_id != session['id']:
        return redirect('/')

    return render_template("sighting_edit.html",user = user, sighting = sighting)

#ACTION route ---------------------------- UPDATE/EDIT
@app.route('/sighting/update/<int:id>', methods = ['POST'])
def update_sighting(id):
    if 'id' not in session:
        return redirect('/') 
    data={
        **request.form,
        'id': id
    }
    if Sighting.validate(request.form):
        Sighting.update_sighting(data)
        return redirect('/welcome')
    return redirect(f'/sighting/edit/{id}')
    
#render route ----------------------------------CREATE
@app.route('/sighting/create')
def create_sighting():
    if 'id' not in session:
        return redirect('/')
    data = {'id': session['id']}
    user = User.lookup_by_id(data)

    return render_template("sighting_create.html", user = user)

#ACTION route ------------------------------------ CREATE
@app.route('/sighting/creating', methods = ['POST'])
def creating_sighting():
    if 'id' not in session:
        return redirect('/')
    data = {
        **request.form,
        'user_id': session['id']
    }
    print(data)
    if Sighting.validate(data):
        new_sighting = Sighting.create(data)
        return redirect('/welcome')
    return redirect(f'/sighting/create')

# ----------------------------------------- DELETE ROUTE
@app.route('/sighting/delete/<int:id>')
def delete_sighting(id):
    if 'id' not in session:
        return redirect('/')
    data = {
        'id': id
    }
    sighting = Sighting.get_sighting_by_id(data)
    if sighting.user_id == session['id']:
        Sighting.delete_sighting(data)
        print(f"deleted sighting {sighting.location}")
    else:
        flash("You are only allowed to delete your own sightings!", "welcome_error")
    return redirect('/welcome')

#----------------------------------------- VIEW ONLY ROUTE
@app.route('/sighting/view/<int:id>')
def view_sighting(id):
    if 'id' not in session:
        return redirect('/')
    data= {
        'id': id
    }
    user_data = {
        'id': session['id']
    }
    user = User.lookup_by_id(user_data)
    sighting = Sighting.get_sighting_by_id(data)
    return render_template("sighting_view.html", user= user, sighting = sighting)

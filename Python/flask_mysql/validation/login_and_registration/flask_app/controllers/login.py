from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user_model import User


@app.route("/")
def index():
    
    return render_template("login.html")

@app.route('/validate_registration', methods = ['POST'])
def val_reg():
    is_valid= User.validate(request.form)
    if is_valid:
    
        user = User.create(request.form)
        session['id'] = user
        return redirect('/welcome')

    return redirect('/')

@app.route('/validate_login', methods = ['POST'])
def val_log():
    form_data = {
        'email': request.form['login_email'],
        'password': request.form['login_pass']
    }
    user = User.lookup_by_email(form_data)
    if user == False:
        flash("Invalid credentials", "login_error")
        return redirect('/')
    
    success = user.validate_login(form_data, user)
    if success:
        session['id'] = user.id
        return redirect('/welcome')
    return redirect('/')


@app.route('/welcome')
def welcome():
    if 'id' in session:
        data = {
            'id': session['id']
        }
        user = User.lookup_by_id(data)
        print(user.first_name)
        return render_template("welcome.html", user = user)
    print("no session")
    return redirect('/')

@app.route('/delete/login/<int:id>')
def delete_login(id):
    data = {
        'id': id
    }
    User.delete(data)
    return redirect('/welcome')

@app.route('/logout')
def logout():
    del session['id']
    return redirect('/')


from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.user import User

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    # print(users)
    return render_template("read.html", users = users)

@app.route('/create')
def create():
    return render_template("create.html")

@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    print(f"data is: {data}")
    # We pass the data dictionary into the save method from the user class.
    user = User.save(data)
    # Don't forget to redirect after saving to the database.
    
    redirect_to= "/display/"
    redirect_to += str(user)
    return redirect(redirect_to)

# displays the user selected ONLY
@app.route('/display/<int:id>')
def display_one(id):
    data = {
        'id': id
    }
    user = User.get_one(data)
    return render_template("show_user.html", user = user)
    

# DISPLAY route for EDITTING USER
@app.route('/edit/<int:id>')
def edit_user(id):
    data = {
        'id': id
    }
    user = User.get_one(data)
    return render_template("edit_user.html", user = user)

#ACTION ROUTE to query DB for EDITTING USER
@app.route('/update/<int:id>', methods = ["POST"])
def update_user(id):
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "id":id
    }
    User.update(data)

    redirect_to= "/display/"
    redirect_to += str(id)
    return redirect(redirect_to)

#Action route -- redirects to home page
@app.route('/delete/<int:id>')
def delete_user(id):
    data = {
        'id': id
    }
    User.delete(data)
    return redirect('/')

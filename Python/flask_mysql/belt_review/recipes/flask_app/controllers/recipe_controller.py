from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe

@app.route('/welcome')
def welcome():
    if 'id' in session:
        data = {
            'id': session['id']
        }
        user = User.lookup_by_id(data)
        print(user.first_name)
        all_recipes = Recipe.get_all()
        return render_template("welcome.html", user = user, all_recipes = all_recipes)
    print("no session")
    return redirect('/')

#display route
@app.route('/recipe/edit/<int:id>')
def edit_recipe(id):
    if 'id' not in session:
        return redirect('/')
    recipe_to_edit = {
        'id': id
    }
    
    recipe = Recipe.get_recipe_by_id(recipe_to_edit)
    if recipe.user_id != session['id']:
        return redirect('/')

    print(recipe.created_at)
    new_date = recipe.created_at
    new_date = Recipe.format_date(new_date)
    recipe.created_at = new_date
    return render_template("recipe_edit.html", recipe = recipe)

#ACTION route -------- UPDATE
@app.route('/recipe/update/<int:id>', methods = ['POST'])
def update_recipe(id):
    if 'id' not in session:
        return redirect('/') 
    data={
        **request.form,
        'id': id
    }
    if Recipe.validate(request.form):
        Recipe.update_recipe(data)
        return redirect('/welcome')
    return redirect(f'/recipe/edit/{id}')
    
#render route --------CREATE
@app.route('/recipe/create')
def create_recipe():
    if 'id' not in session:
        return redirect('/')
    data = {'id': session['id']}
    user = User.lookup_by_id(data)

    return render_template("recipe_create.html", user = user)

#ACTION route -------- CREATE
@app.route('/recipe/creating', methods = ['POST'])
def creating_recipe():
    if 'id' not in session:
        return redirect('/')
    data = {
        **request.form,
        'user_id': session['id']
    }
    if Recipe.validate(data):
        new_recipe = Recipe.create(data)
        return redirect(f'/recipe/view/{new_recipe}')
    return redirect(f'/recipe/create')

@app.route('/recipe/delete/<int:id>')
def delete_recipe(id):
    if 'id' not in session:
        return redirect('/')
    data = {
        'id': id
    }
    recipe = Recipe.get_recipe_by_id(data)
    if recipe.user_id == session['id']:
        Recipe.delete_recipe(data)
        print(f"deleted recipe {recipe.name}")
    flash("You are only allowed to delete your own recipes!", "welcome_error")
    return redirect('/welcome')

@app.route('/recipe/view/<int:id>')
def view_recipe(id):
    if 'id' not in session:
        return redirect('/')
    data = {
        'id': id
    }
    user = User.lookup_by_id(data)
    recipe = Recipe.get_recipe_by_id(data)
    return render_template("recipe_view.html", user= user, recipe = recipe)

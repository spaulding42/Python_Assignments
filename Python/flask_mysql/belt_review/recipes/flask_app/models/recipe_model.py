from sqlite3 import connect
from .. import DATABASE
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import render_template,redirect,request,session,flash
from flask_app.models import user_model


class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.under_30 = data['under_30']
        self.description = data['description']
        self.instructions = data['instructions']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.created_by = []
    @classmethod
    def create(cls,data):
        query = "insert into recipes (name, under_30, description, instructions, user_id, created_at) VALUES (%(name)s, %(under_30)s, %(description)s, %(instructions)s, %(user_id)s, %(created_at)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id WHERE users.id = recipes.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_recipes = []
        for recipe in results:
            user_data = {
                    **recipe,
                    'id': recipe['users.id'],
                    'created_at': recipe['users.created_at'],
                    'updated_at': recipe['users.updated_at']
                }
            recipe_instance = cls(recipe)
            recipe_instance.created_by = user_model.User.lookup_by_id(user_data)
            all_recipes.append(recipe_instance)
        print(f"list of all the recipes: {all_recipes}")
        return all_recipes

    @classmethod
    def get_recipe_by_id(cls,data):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            user_data = {
                    **results[0],
                    'id': results[0]['users.id'],
                    'created_at': results[0]['users.created_at'],
                    'updated_at': results[0]['users.updated_at']
                    }
            recipe = cls(results[0])
            recipe.created_by = user_model.User.lookup_by_id(user_data)
            return recipe
    
    @classmethod
    def update_recipe(cls,data):
        query = "UPDATE recipes SET name = %(name)s, under_30 = %(under_30)s, description = %(description)s, instructions = %(instructions)s, created_at = %(created_at)s WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate(data):
        print(f" printing data {data}")
        is_valid = True
        if len(data['name']) < 1:
            flash('Name of dish is required', "recipe_error")
            is_valid = False
        if len(data['description']) < 1:
            flash("Description is required!", "recipe_error")
            is_valid = False
        if len(data['instructions']) < 1:
            flash("Instructions is required", "recipe_error")
            is_valid = False
        if data['created_at'] == '':
            print("missing creation date!!!!!!!!!!!!!!!!!!")
            flash("date is required", "recipe_error")
            is_valid = False
        if 'under_30' not in data:
            flash("Under 30 minutes is required!", "recipe_error")
            is_valid=False

        return is_valid

    @staticmethod
    def format_date(data):
        date = str(data)
        new_date = ""
        for i in date:
            if i == " ":
                break
            new_date+= i
        print(new_date)
        return new_date

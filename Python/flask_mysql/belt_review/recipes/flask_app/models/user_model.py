from .. import DATABASE
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import render_template,redirect,request,session,flash
from flask_app.models import recipe_model
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls,data):
        data_hashed = {
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'email': data['email'],
            'password': bcrypt.generate_password_hash(data['password'])
        }
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db(query, data_hashed)

    @classmethod
    def lookup_by_email(cls, data):
        query = "SELECT * FROM  users WHERE email = %(email)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        print(results)
        if results:
            user_instance = cls(results[0])
            print("user_instance")
            return user_instance
        print("returning False!!!!!!!!!!!!!!!!!!!!")
        return False

    @classmethod
    def lookup_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:
            user = cls(results[0])
            return user
        return False
        
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s"
        connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['first_name']) < 2:
            flash('First Name must be 2 or more characters', "reg_error")
            is_valid = False
        if len(data['last_name']) <2:
            flash('Last Name must be 2 or more characters', "reg_error")
            is_valid = False
        if len(data['email']) < 1:
            flash('Email is required', "reg_error")
            is_valid = False
        if len(data['password']) < 8:
            flash('Password must be at least 8 characters long', "reg_error")
            is_valid = False
        if (data['password'] != data['confirm_pass']):
            flash('Passwords do not match', "reg_error")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!", "reg_error")
            is_valid = False
        if User.lookup_by_email(data) != False:
            flash("Email already exists!", "reg_error")
            is_valid=False
        return is_valid

    @staticmethod
    def validate_login(form_data,user):
        if form_data['email'] == user.email and bcrypt.check_password_hash(user.password, form_data['password']):
            return True
        flash("Invalid Credentials", "login_error")
        return False
        
    
        

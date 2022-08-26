
from .. import DATABASE
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import render_template,redirect,request,session,flash
from flask_app.models import user_model


class Sighting:
    def __init__(self,data):
        self.id = data['id']
        self.location = data['location']
        self.description = data['description']
        self.sasquatches = data['sasquatches']
        self.date_seen = data['date_seen']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.created_by = []
    @classmethod
    def create(cls,data):
        query = "INSERT INTO sightings (location, description, sasquatches, date_seen, user_id) VALUES (%(location)s, %(description)s, %(sasquatches)s, %(date_seen)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM sightings JOIN users ON sightings.user_id = users.id WHERE users.id = sightings.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_sightings = []
        for sighting in results:
            user_data = {
                    **sighting,
                    'id': sighting['users.id'],
                    'created_at': sighting['users.created_at'],
                    'updated_at': sighting['users.updated_at']
                }
            sighting_instance = cls(sighting)
            sighting_instance.created_by = user_model.User.lookup_by_id(user_data)
            all_sightings.append(sighting_instance)
        print(f"list of all the sightings: {all_sightings}")
        return all_sightings

    @classmethod
    def get_sighting_by_id(cls,data):
        query = "SELECT * FROM sightings JOIN users ON sightings.user_id = users.id WHERE sightings.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            user_data = {
                    **results[0],
                    'id': results[0]['users.id'],
                    'created_at': results[0]['users.created_at'],
                    'updated_at': results[0]['users.updated_at']
                    }
            sighting = cls(results[0])
            sighting.created_by = user_model.User.lookup_by_id(user_data)
            return sighting
    
    @classmethod
    def update_sighting(cls,data):
        query = "UPDATE sightings SET location = %(location)s, description = %(description)s, sasquatches = %(sasquatches)s, date_seen = %(date_seen)s WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_sighting(cls, data):
        query = "DELETE FROM sightings WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate(data):
        print(f" printing data {data}")
        is_valid = True
        if len(data['location']) < 1:
            flash('Location is required', "sighting_error")
            is_valid = False
        if len(data['description']) < 1:
            flash("Description is required!", "sighting_error")
            is_valid = False
        if len(data['date_seen']) < 1:
            flash("Date seen is required", "sighting_error")
            is_valid = False
        if data['sasquatches'] == '':
            flash("You can't report a Sasquatch if there were no Sasquatches present!", "sighting_error")
            is_valid = False
        elif int(data['sasquatches']) < 1:
            flash("You can't report a Sasquatch if there were no Sasquatches present!", "sighting_error")
            is_valid = False
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

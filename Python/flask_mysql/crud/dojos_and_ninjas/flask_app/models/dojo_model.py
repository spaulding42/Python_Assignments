from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import ninja_model

class Dojo:
    def __init__(self,data):
            self.id = data['id']
            self.name = data['name']
            self.created_at = data['created_at']
            self.updated_at = data['updated_at']
            
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dojos;'
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        dojos = []
        # Iterate over the db results and create instances of user with cls.
        for dojo in results:
            dojo_instance = cls(dojo)
            dojos.append(dojo_instance)
        print(f"List of all the dojos: {dojos}")
        return dojos

    @classmethod
    def add_dojo(cls, data ):
        print("did i make it?---------------------------------")
        query = "INSERT INTO dojos ( name ) VALUES ( %(name)s);"
        
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def list_one_dojo(cls, data):
        query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        # if the result of combining the dojo with the ninjas returns a list:
        if results:
            dojos_with_ninjas = []
            # unpack the data from results into a list of dicts that can then be passed outside of the function
            # without this it will return a list of Dojos which it wont know what to do with outside of the model
            for row_in_db in results:
                print(f"printing row_in_db:---------------\n {row_in_db}")
                ninja_data = {
                    'id': row_in_db['ninjas.id'],
                    'first_name': row_in_db['first_name'],
                    'last_name': row_in_db['last_name'] ,
                    'age': row_in_db['age'],
                    'created_at': row_in_db['ninjas.created_at'],
                    'updated_at': row_in_db['ninjas.updated_at'],
                    'name': row_in_db['name'] #this name is actually the name of the Dojo which the ninja belongs to. Will need this passed to display the dojo name as the header
                }
                #adds an instance of the ninja_data(1 ninja) onto the current list of ninja_data(all ninjas in dojo)
                dojos_with_ninjas.append(ninja_data)
            return dojos_with_ninjas
        return data

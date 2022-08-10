from flask import Flask, render_template  # Import Flask to allow us to create our app
users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def starting():
    return render_template("index.html", users=users)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)
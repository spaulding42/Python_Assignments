from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def starting():
    return "in url type /color1/color2/height/width"

@app.route('/<color_1>/<color_2>/<int:height>/<int:width>')
def play(color_1,color_2,height,width):
    return render_template("index.html", color_1=color_1, color_2=color_2, height=height, width=width)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)
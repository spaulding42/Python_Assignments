from flask import Flask, render_template, request, redirect, session # added request
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def starting():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
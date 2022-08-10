from flask import Flask, render_template, request, redirect, session # added request
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def starting():
    return render_template("index.html")



@app.route('/process', methods = ['POST'])
def process():
    session['name'] = request.form['name']
    session['location']= request.form['location']
    session['language']= request.form['language']
    session['comments']= request.form['comments']

    # need to collect all form data then check to see if/what fruit was checked
    all_values= request.form
    fruits = []
    if 'pineapple' in all_values:
        fruits.append(" Pineapple")
        print ("pineapple was checked")
    if 'bananas' in all_values:
        fruits.append(" Bananas")
        print("bananas was checked")
    if 'strawberries' in all_values:
        fruits.append(" Strawberries")
        print("strawberries was checked")
    session['fruits'] = fruits

    #contingency if they never enter a name
    if session['name'] == '':
        session['name'] = '<no name>'
    if session['comments'] == '':
        session['comments'] = '<no comment>'

    return redirect('/result')



@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)
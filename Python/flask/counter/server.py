from flask import Flask, render_template, request, redirect, session # added request
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


# our index route will handle rendering our form
@app.route('/')
def index():
    if 'count' in session:
        print('key exists!')
        session['count'] += 1
    else:
        session['count'] = 1
        print("key 'count' does NOT exist")
        
    return render_template("index.html", count = session['count'])



@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')




@app.route('/clicked', methods = ['POST'])
def clicked():
    #store the value passed from hidden form to know which button was clicked
    which_one = request.form['which_button']
    
    # 'Add two' button clicked do this
    if which_one == 'add':
        print("clicked add")
        session['count'] += 1
        return redirect('/')

    # reset visits button clicked do this
    elif which_one == 'clear':
        print("clicked clear")
        return redirect('/destroy_session')

    else:
        print("crap")
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
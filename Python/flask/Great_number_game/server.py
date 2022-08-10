from flask import Flask, render_template, request, redirect, session # added request
import random

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def starting():
    session['number'] = random.randint(1,100)
    print(f"Number to be guessed: {session['number']}")
    session['high_so_far'] = []
    session['low_so_far'] = []
    session['started'] = False
    session['guess_count'] = 0
    session['game_lost'] = False
    session['color'] = 'green'
    return render_template("index.html")

@app.route('/process', methods=["POST"])
def process():
    print(request.form)

    if request.form['guess'] == '' and session['started'] == False:      # if nothing is entered and the game hasn't started yet
        print("no guess entered while game not started. redirecting back to the start and making a new number to be guessed")
        return redirect('/')
    elif request.form['guess'] == '' and session['started'] == True:     # if nothing is entered during the game
        print("nothing entered while game in progress. redirecting back to the game started screen. number to be guessed doesn't change")
        return redirect('/game_started')
    else:                                                                # Valid Guess. Checks to see if the guess is high or low or just right
        guess = int(request.form['guess'])
        guessedhigh = session['high_so_far']
        guessedlow = session['low_so_far']
        if guess > session['number']:                            # checks to see is the guess is HIGHER
            session['high_low'] = "high"
            guessedhigh.append(guess)
            session['high_so_far'] = guessedhigh
            print(guessedhigh)
            session['guess_count'] += 1
            if session['guess_count'] > 5:             #checks if they have exceeded their guess count
                session['game_lost'] = True
                return redirect('/game_ended')
            else:
                return redirect('/game_started')
        if guess < session['number']:                              #checks to see if the guess is LOWER
            session['high_low'] = "low"
            guessedlow.append(guess)
            session['low_so_far'] = guessedlow
            print(guessedlow)
            session['guess_count'] += 1
            if session['guess_count'] > 5:             #checks if they have exceeded their guess count
                session['game_lost'] = True
                return redirect('/game_ended')
            else:
                return redirect('/game_started')
        if guess == session['number']:
            print("guessed number")
            return redirect('/game_ended')


@app.route('/game_started')
def game_started():
    session['started'] = True
    return render_template('game_started.html')


@app.route('/game_ended')
def game_ended():
    if session['game_lost'] == False:
        session['end_msg'] = f"You guessed it with {session['guess_count'] +1 } guesses! The number was {session['number']}!"
        return render_template("game_ended.html")
    else:
        session['end_msg'] = f"You Lose!"
        session['color'] = 'red'
        return render_template("game_ended.html")


if __name__ == "__main__":
    app.run(debug=True)
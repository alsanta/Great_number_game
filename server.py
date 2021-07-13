from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = '555'

@app.route('/')
def main():
    session['number'] = random.randint(1,100)
    print(session['number'])
    return render_template('index.html', number = int(session['number']), guess=0)

@app.route('/guess', methods=['POST'])
def guess():
    session['guess']= request.form['numberGuess']
    print(session['number'])
    return render_template('index.html', number = int(session['number']), guess = int(session['guess']))

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
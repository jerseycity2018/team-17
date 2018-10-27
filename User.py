from flask import Flask, flash, request, redirect, render_template, session, abort
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('login_test.html')

@app.route('/login', methods=['POST'])
def login():
	if request.form['password'] == 'password' and request.form['username'] == 'admin':
		session['logged_in'] = True
	else:
		flash('wrong password!')
	return 'Done'

	

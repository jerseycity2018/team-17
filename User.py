from flask import Flask, flash, request, redirect, render_template, session, abort
from flask_bootstrap import Bootstrap
import os
import json

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
#	with open('user_data.json') as json_user_data:
#		d = json.load(json_user_data)
	return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
	username = request.form['username']
	password = request.form['password']
	print(username)
	print(password)
	result = check(username, password)
	if result == True:
		return render_template('profile.html', )
	else:
		error = "wrong password or username"
		print(error)
	return render_template('login.html', error=error)

@app.route('/loadlogin', methods=['GET','POST'])
def dashboard():
	if request.method=='GET':
		return render_template('login.html')
	

def check(username, password):
	with open('users.json') as json_user_data :
		d = json.load(json_user_data)
		for users in d['users']:
			if users['username']==username and users['password']==password:
				return True 
	return False






#def checkUser(username, password):
#	rs = c.execute("SELECT * FROM username_tbl WHERE username = %s AND password = %s", (username, password))
#	# rs = con.execute("SELECT * FROM beers")
#	result = rs.first()
#	if result is None:
#		return None
#	else:
#		print(result)
#		return result 

	

from flask import Flask, flash, request, redirect, render_template, session, abort
from flask_bootstrap import Bootstrap
#from flask.ext.scss import Scss
import json

#conn = sqlite3.connect("pathtofilehere")
#c = conn.cursor

app = Flask(__name__)
Bootstrap(app)
#Scss(app, static_dir='static', asset_dir='assests')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
	username = request.form['username']
	password = request.form['password']
	print(username)
	print(password)
	result = check(username, password)
	if result == True:
		return render_template('index.html')
	else:
		error = "wrong password or username"
		print(error)
	return render_template('index.html', error=error)

@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
	if requests.method=='GET':
		username = request.form['username']
		result = getData(username)
	

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

	

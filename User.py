from flask import Flask, flash, request, redirect, render_template, session, abort
import sqlite3
#from sqlalchemy import create_engine
#from sqlalchemy import sql

conn = sqlite3.connect("pathtofilehere")
c = conn.cursor

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('login_test.html')

@app.route('/login', methods=['POST'])
def login():
	username = request.form['username']
	password = request.form['password']
	print(username)
	print(password)
	user = checkUser(username, password)
	if user is not None :
		return render_template('index.html')
	else:
		error = "wrong password or username"
		print(error)
	return render_template('index.html', error=error)

def checkUser(username, password):
	rs = c.execute("SELECT * FROM username_tbl WHERE username = %s AND password = %s", (username, password))
	# rs = con.execute("SELECT * FROM beers")
	result = rs.first()
	if result is None:
		return None
	else:
		print(result)
		return result 

	

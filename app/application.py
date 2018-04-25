from flask import Flask, render_template, request
import sqlite3
import hashlib
import sys

# --- SET UP ---

app = Flask(__name__)
user_data_db = "user_data.sqlite"
accounts_db = "accounts.sqlite"
cwd = os.path.dirname(os.path.realpath(__file__))

# --- MODULES ---

""" this function creates a new table in the user_data database the store a users tasks and the status of those tasks """

def create_task_table_for_user(account_id):
	conn = sqlite3.connect(cwd + "/" + user_data_db) # opens the user_data database
	c = conn.cursor() # sets up a cursor
	exit_code = 0
	try:
		c.execute("""CREATE TABLE ?(task TEXT NOT NULL, status BOOL NOT NULL)""",[account_id,]) # creates a new table based on the account id
		exit_code = 1
	except Exception as e:
		print("create_task_table_user !!! " + e, file=sys.stderr)
		exit_code = 0
	conn.commit() # commits and saves the changes
	return exit_code
	
""" this function generates a new unique account id, based on the email and using the sha256 method of encoding """

def generate_account_id(email):
	sha = hashlib.sha256().update(str(email).encode('utf-8')) # updates the haslib library with a new email to hash
	return sha.hexdigest() # returns the sha256 hashed version of the email

""" this function takes care of setting up a new user: adding to databases creating tables and generating unique id """

def create_new_user(name, email, password):
	conn = sqlite3.connect(cwd + "/" + accounts_db) # opens the accounts db to add a new user
	c = conn.cursor() # sets up a cursor
	new_id = generate_account_id(email)
	c.execute("""INSERT INTO account_data(id, name, email, password) VALUES (?, ?, ?, ?)""",[new_id, name, email, password])
	conn.commit() # commits and saves changes
	create_task_table_for_user(new_id) # add error handling for this function call
	return new_id

""" this function returns a list of tasks based a users account_id """

def get_tasks(account_id):
	pass

# --- ROUTES ---

@app.route("/", methods = ['POST', 'GET'])
def index():
	return render_template("index.html")

@app.route("/signup", methods = ['POST', 'GET'])
def sign_up():
	if request.method == 'GET':
		pass
	elif request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		password = request.form['password']
		create_user_ec = create_new_user(name, email, password)
		if create_user_ec != 0: # 
			tasks = get_user_tasks(account_id)
			render_template("dashboard.html", )
		else:
			# add error handling here
			pass

if __name__ == '__main__':
	app.run(port=80, host='0.0.0.0')


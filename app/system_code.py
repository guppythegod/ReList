import sqlite3
import sys
import os

#! --- SET UP ---

user_data_db = "user_data.sqlite"
accounts_db = "accounts.sqlite"
cwd = os.path.dirname(os.path.realpath(__file__))

#! --- MODULES ---

""" this function creates a new table in the user_data database the store a users tasks and the status of those tasks """

def create_task_table_for_user(email):
	conn = sqlite3.connect(cwd + "/" + user_data_db) # opens the user_data database
	c = conn.cursor() # sets up a cursor
	exit_code = 0
	try:
		c.execute("""CREATE TABLE ? (task TEXT NOT NULL, status INT NOT NULL);""",[email,]) # creates a new table based on the account id
		exit_code = 1
	except sqlite3.IntegrityError as e:
		pass
	conn.commit() # commits and saves the changes
	return exit_code

""" this function takes care of setting up a new user: adding to databases creating tables and generating unique id """

def create_new_user(name, email, password):
	print("at create user", file=sys.stderr)
	exit_code = 0
	conn = sqlite3.connect(cwd + "/" + accounts_db) # opens the accounts db to add a new user
	c = conn.cursor() # sets up a cursor
	print("connected to db", file=sys.stderr)
	try:
		c.execute("""INSERT INTO account_data(email, name, password) VALUES (?, ?, ?)""",[email, name, password])
	except sqlite3.IntegrityError as e:
		pass
	print("c.execute worked", file=sys.stderr)
	conn.commit() # commits and saves changes
	create_table_ec = create_task_table_for_user(email) # add error handling for this function call
	if create_new_user == 1:
		exit_code = 0
	return exit_code

""" this function returns a list of tasks based a users account_id """

def get_tasks(account_id):
	conn = sqlite3.connect(cwd + "/" + user_data_db) # opens the user_data database
	c = conn.cursor() # sets up a cursor
	c.execute("""FROM ? SELECT tasks WHERE status = 1""",[account_id])
	task_list = []
	fetched = c.fetchall()
	for i in range(len(fetched)):
		pass
	
def complete_task(account_id, task_id):
	pass

def create_task(account_id, task_name):
	pass


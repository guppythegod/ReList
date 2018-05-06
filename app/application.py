from flask import Flask, request, render_template
import system_code
import sys

#! --- SET UP ---

app = Flask(__name__) 

#! --- ROUTES ---

@app.route("/", methods = ['POST', 'GET'])
def index():
	return render_template("index.html")

@app.route("/signup", methods = ['POST', 'GET'])
def sign_up():
	print("at signup", file=sys.stderr)
	if request.method == 'GET':
		return render_template("signup.html")
	elif request.method == 'POST':
		print("attempted post at signup", file=sys.stderr)
		name = request.form['first'] + " " + request.form['last']
		print(name, file=sys.stderr)
		email = request.form['email']
		print(email, file=sys.stderr)
		password = request.form['password']
		print(email + " " + password, file=sys.stderr)
		create_user_ec = system_code.create_new_user(name, email, password)
		print(create_user_ec, file=sys.stderr)
		if create_user_ec != 0: # 
			#tasks = a.get_user_tasks(account_id)
			return render_template("dashboard.html")
		else:
			# add error handling here
			return "error"

#@app.route("/login", )

if __name__ == '__main__':
	app.run(port=80)
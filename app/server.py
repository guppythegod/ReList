from flask import Flask, request, render_template
import application as a

#! --- SET UP ---

app = Flask(__name__) 

#! --- ROUTES ---

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
		create_user_ec = a.create_new_user(name, email, password)
		if create_user_ec != 0: # 
			tasks = a.get_user_tasks(account_id)
			render_template("dashboard.html", )
		else:
			# add error handling here
			pass

if __name__ == '__main__':
	app.run(port=80)
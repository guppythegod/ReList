from flask import Flask, render_template
import sqlite3

# --- SET UP ---

app = Flask(__name__)
sqlite_file = "user_data.sqlite"
cwd = os.path.dirname(os.path.realpath(__file__))

# --- MODULES ---

def create_table_for_user(account_id):
	conn = sqlite3.connect(cwd + "/" + sqlite_file)
	c = conn.cursor()
	c.execute("""CREATE TABLE ?()""",[])

# --- ROUTES ---

@app.route("/")
def index():
	return render_template("index.html")

if __name__ == '__main__':
	app.run(port=80, host='0.0.0.0')


import flask as fl
from flask import render_template
import sqlite3

DATABASE = 'data/b.db'

app = fl.Flask(__name__)
#-----------------------------------------------------------#
#database#
def get_db():
  db = getattr(fl.g, '_database', None)
  if db is None:
    db = fl.g._database = sqlite3.connect(DATABASE)
  return db

@app.teardown_appcontext
def close_connection(exception):
  db = getattr(fl.g, '_database', None)
  if db is not None:
    db.close()
    
#-----------------------------------------------------------#

@app.route("/")
def root():
    return render_template('index.html')

@app.route("/database", methods=["GET","POST"])
def hello():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM mytable") 
    return str(cur.fetchall())

@app.route("/name", methods=["GET", "POST"])
def name():
    return "Hello " + fl.request.form["name"] + "!"

@app.route("/info")
def information():
    return "Welcome to Operating Systems Notes. Use this single page web application to store all your information on OS" + fl.request.form["info"]

if __name__ == "__main__":
    app.run(debug=True)
import flask as fl
from flask import render_template, request
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
def database():
    dur = post_db().cursor()
    dur.execute("insert into mytable(title,define)",(fl.request.form["title"],fl.request.form["define"]))
    cur = get_db().cursor()
    cur.execute("Select * from mytable")
    return str(cur.fetchall()) + str(dur.fetchall()) + render_template('base.html')

@app.route("/name", methods=["GET", "POST"])
def name():
    return fl.request.form["name"] + " : " + fl.request.form["comment"]

@app.route("/info", methods=["GET","POST"])
def info():
    return render_template('base.html') + "Welcome to Operating Systems Notes. Use this single page web application to store all your information on OS"

if __name__ == "__main__":
    app.run(debug=True)
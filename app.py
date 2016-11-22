import flask as fl
from flask import render_template, request, g
import sqlite3
#-----------------------------------------------------------#

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
#home page#
@app.route("/")
def root():
    return render_template('index.html')

#-----------------------------------------------------------#
#inserting data into database#
@app.route("/database", methods=["GET","POST"])
def database():
    cur = get_db().cursor()
    conn = sqlite3.connect(DATABASE)
    curCon = conn.cursor()
    curCon.execute('INSERT INTO mytable(title, define) VALUES(?,?)',(fl.request.form['title'],fl.request.form['define']))
    conn.commit()
    conn.close()
    cur.execute("Select * from mytable")
    return (render_template('base.html') + str(cur.fetchall()) ) 

@app.route("/databaseStore",methods=["GET","POST"])
def databaseStore():
    cur = get_db().cursor()
    cur.execute("Select * from mytable")
    return (render_template('base.html') + str(cur.fetchall()))

#-----------------------------------------------------------#
#first dummy info to page
#@app.route("/name", methods=["GET", "POST"])
#def hello():
    #return render_template('base.html') + fl.request.form["name"] + " : " + fl.request.form["comment"]

#-----------------------------------------------------------#
#information on page#

#-----------------------------------------------------------#
@app.route("/info", methods=["GET","POST"])
def info():
    return render_template('base.html') + "Welcome to Operating Systems Notes. Use this single page web application to store all your information on OS"

#-----------------------------------------------------------#

if __name__ == "__main__":
    app.run(debug=True)
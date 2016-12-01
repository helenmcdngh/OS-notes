# Single Page Web Application Project
#### Data Representation and Querying Project 2016

### Project Overview
I have created a Single-Page Web Application that allows you to enter Operating Systems Definitions into a Database, that I adapted from an example project that we were shown throughout the course [sqlite3 example webapp with Flask](https://github.com/data-representation/example-sqlite). It is a very simple designed Application and is also easy to use. 
### How to run this Application
This note recording Application is written using the [Flask](http://flask.pocoo.org/) library in [Python 3](https://www.python.org) and it uses [Bootstrap](http://getbootstrap.com/) links in the html pages for design.
I use the [sqlite3](https://docs.python.org/2/library/sqlite3.html) package for persistence in the Application.
This must also be installed, there is no further installation needed because the database is fully contained in the data directory.

Once all the above requirements are installed, the Application can be run locally:
```bash
$ python databaseSetup.py
```
```bash
$ python app.py
```
Once the Application is running, it can be accessed by pointing your browser at http://127.0.0.1:5000/ .

The Application is simple to use, you simple enter the Definition into the form first the title and then the explanation in the boxes, then click the "Enter to Database" button to submit the Definition to the Database. The Application will then displays the database. The definition will be then saved to the database when you reopen the app. 

### Architecture
This web application runs in [Python 3](https://www.python.org) using the [Flask](http://flask.pocoo.org/) web micro-framework and uses [SQLite3](https://docs.python.org/2/library/sqlite3.html) as a database to store all the definitions.
Python 3 and Flask were requirements for the project. You had a choice between counchDB, mongoDB, Neo4j, Redis and SqLite, I decided to use SQLite as it is easy to use and does not require much setup to get the Web Application up and running.

The Application contains two templates the main template, index.html contains a navigation bar that allows you select to view the form and the database page and the bar also collapses when the browser window is shrunk, it also contains the form to input the data. The other template, base.html is just a basic template that contains the navigation bar that allows you to navigate through the Application. 

I adapted the files setup.py and webapp.py from [sqlite3 example webapp with Flask](https://github.com/data-representation/example-sqlite) for my databaseSetup.py and app.py files in my project. 


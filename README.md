# Single Page Web Application Project
#### Data Representation and Querying Project 2016

### Project Overview
I have created a Single-Page Web Application that allows you to enter Operating Systems Definitions into a Database. It is a very simple designed application and is also easy to use.

### How to run this application
This note recording application is written using the [Flask](http://flask.pocoo.org/) library in [Python 3](https://www.python.org) and it uses bootstrap links in the html pages for design.

I use the [sqlite3](https://docs.python.org/2/library/sqlite3.html) package for persistence in the application.
This must also be installed.
However, no further configuration our setup is required, as the database is fully contained in the db directory in this repository.

Once these prerequisites are installed, the application can be run locally:
```bash
$ python databaseSetup.py
```
```bash
$ python app.py
```
Once the application is running, it can be accessed by pointing your browser at http://127.0.0.1:5000/ .

### Architecture
This web application runs in [Python 3](https://www.python.org) using the [Flask](http://flask.pocoo.org/) web micro-framework and uses SQLite as a database.
Python 3 and Flask were requirements for the project, but SQLite was selected by the team.
I chose SQLite as it is easy to use and does not require much setup to get the web application up and running.


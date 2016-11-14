import sqlite3

DATABASE = 'data/b.db'

def setup_db():
    """Creates database if it has not already been set up."""
    db = sqlite3.connect(DATABASE)
    cur = db.cursor()
    dur = post_db().cursor()
    
    # Create the table if it doesn't exist.
    cur.execute("CREATE TABLE IF NOT EXISTS mytable(id INTEGER PRIMARY KEY, title TEXT, define Text)")
    db.commit()
    
    # Insert some dummy data if the table is empty.
    cur.execute("SELECT COUNT(*) FROM mytable")
    if cur.fetchall()[0][0] == 0:
            cur.execute('INSERT INTO mytable(title, define) VALUES("Deadlock", "When two or more programs, become deadlocked, when each of them is doing nothing while waiting for a resource, occupied by another program, in the same set. ")')
            dur.execute("insert into mytable(title,define",(fl.request.form["title"],fl.request.form["define"]))
            db.commit()

if __name__ == "__main__":
  setup_db()
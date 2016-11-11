import sqlite3

DATABASE = 'data/b.db'

def setup_db():
    """Creates database if it has not already been set up."""
    db = sqlite3.connect(DATABASE)
    cur = db.cursor()

    # Create the table if it doesn't exist.
    cur.execute("CREATE TABLE IF NOT EXISTS mytable(id INTEGER PRIMARY KEY, title TEXT, define Text)")
    db.commit()
    
    # Insert some dummy data if the table is empty.
    cur.execute("SELECT COUNT(*) FROM mytable")
    if cur.fetchall()[0][0] == 0:
            cur.execute('INSERT INTO mytable(title, define) VALUES("Deadlock", "When two or more programs, become deadlocked, when each of them is doing nothing while waiting for a resource, occupied by another program, in the same set. ")')
            cur.execute('INSERT INTO mytable(title, define) VALUES("Starvation", "Is a problem encountered in concurrent computing where a process is perpetually denied necessary resources to process its work")')
            cur.execute('INSERT INTO mytable(title, define) VALUES("Long term scheduling", "It is also called a job scheduler. A long-term scheduler determines which programs are admitted to the system for processing. It selects processes from the queue and loads them into memory for execution. Process loads into the memory for CPU scheduling.")')
    db.commit()

if __name__ == "__main__":
  setup_db()
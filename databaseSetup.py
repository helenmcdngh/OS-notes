import sqlite3

DATABASE = 'data/b.db'
#setuping up database
def setup_db():
    db = sqlite3.connect(DATABASE)
    cur = db.cursor()
    
    #creating a table for database
    cur.execute("CREATE TABLE IF NOT EXISTS mytable( title TEXT, define TEXT)")
    db.commit()
    
    #Inserting data into tables database
    cur.execute("SELECT COUNT(*) FROM mytable")
    if cur.fetchall()[0][0] == 0:
            #inserting definition
            cur.execute('INSERT INTO mytable(title, define) VALUES("Deadlock", "When two or more programs, become deadlocked, when each of them is doing nothing while waiting for a resource, occupied by another program, in the same set. ")')
            db.commit()

if __name__ == "__main__":
  setup_db()
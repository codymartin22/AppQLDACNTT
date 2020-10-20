import sqlite3
class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, "
                    "author TEXT, year INTEGER, isbn INTEGER, amount INTEGER, cost INTEGER)")
        self.conn.commit()

    def insert(self,title, author, year, isbn, amount, cost):
        #the NULL parameter is for the auto-incremented id
        self.cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?,?,?)", (title,author,year,isbn, amount, cost))
        self.conn.commit()


    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()

        return rows

    def search(self,title="", author="", year="", isbn="", amount="",cost=""):
        self.cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? "
                    "OR isbn = ? OR amount = ? OR cost = ?", (title, author, year, isbn, amount, cost))
        rows = self.cur.fetchall()
        #conn.close()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id = ?", (id,))
        self.conn.commit()
        #conn.close()

    def update(self,id, title, author, year, isbn,amount,cost):
        self.cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ?, amount = ?, cost = ? WHERE id = ?", (title, author, year, isbn, amount, cost, id))
        self.conn.commit()

    #destructor-->now we close the connection to our database here
    def __del__(self):
        self.conn.close()

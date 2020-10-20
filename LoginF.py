# db la : userInfo.db
import sqlite3
class LoginF:
                def __init__(self,db):
                                self.conn = sqlite3.connect(db)
                                self.cur = self.conn.cursor()
                                self.cur.execute("CREATE TABLE IF NOT EXISTS LoginInfo (username TEXT  PRIMARY KEY, password TEXT)")
                                self.conn.commit()
                def Login(self,username="",password=""):
                                self.cur.execute("SELECT * FROM LoginInfo WHERE username = '"+username+"' and password = '"+password+"'")
                                rows = self.cur.fetchall()
                                #conn.close()
                                return len(rows)
                def Register(self,username="",password="",repassword=""):
                                if (password != repassword):return 0
                                elif (self.CheckUsername(username) > 0): return 1
                                else:
                                                self.cur.execute("INSERT INTO LoginInfo VALUES('"+username+"','"+password+"')")
                                                self.conn.commit()
                                                return 2

                def CheckUsername(self,username=""):
                                self.cur.execute("SELECT * FROM LoginInfo WHERE username = '"+username+"' ")
                                rows = self.cur.fetchall()
                                #conn.close()
                                return len(rows)


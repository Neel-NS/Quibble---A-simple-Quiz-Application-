import mysql.connector


class DbHelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost", username="root", password="", database="quiz")
            self.mycursor = self.conn.cursor()
        except:
            print("Database Error!")
        else:
            print("Connected to Database Successfully!")

    def register(self, name, username, email, password):
        try:
            self.mycursor.execute("INSERT INTO users VALUES(NULL, '{}', '{}', '{}','{}')".format(name, username, email,
                                                                                                 password))
            self.conn.commit()
        except:
            return -1
        else:
            return 1

    def search(self, username, password):
        self.mycursor.execute("SELECT * FROM users WHERE username LIKE '{}' AND password LIKE '{}'".format(username,
                                                                                                           password))
        data = self.mycursor.fetchall()
        return data

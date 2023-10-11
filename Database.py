import sqlite3
from PIL import Image
import io, os


class Database:
    def __init__(self):
        self.db = sqlite3.connect('Database.sqlite3')
        self.cursor = self.db.cursor()
        self.tables()

    def tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS User (
                                                            username TEXT,
                                                            email TEXT,
                                                            PhoneNo TEXT,
                                                            Password TEXT
                                                        )''')

    def user_table(self, name, email, Phone, Password):
        self.cursor.execute("INSERT INTO User (username, email, PhoneNo, Password)"
                            "VALUES (?, ?, ?, ?)", (name, email, Phone, Password))
        self.db.commit()

    def check_email(self, email, table_name, email_column):
        query = f"SELECT * FROM {table_name} WHERE {email_column} = ?"
        self.cursor.execute(query, (email,))
        if self.cursor.fetchone() is not None:
            return True
        else:
            return False

    def check_present(self, email, password, table_name, email_column, password_column):
        query = f"SELECT * FROM {table_name} WHERE {email_column} = ? AND {password_column} = ?"
        self.cursor.execute(query, (email, password))
        if self.cursor.fetchone() is not None:
            return True
        else:
            return False

    def get_data(self, mail):
        query = "SELECT username, email, PhoneNo  FROM User WHERE email = ?"
        params = (mail,)
        self.cursor.execute(query, params)
        result = self.cursor.fetchone()
        if result is not None:
            name = result[0]
            mail = result[1]
            contact = result[2]
            return name, mail, contact
        self.db.close()



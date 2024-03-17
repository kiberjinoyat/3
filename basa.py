import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("Muhammadjon.db")
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            create table if not exists user(
                id integer primary key ,
                username varchar not null ,
                password varchar not null ,
                email varchar ,
                country varchar ,
                age integer ,
                phone_number varchar not null )
        """)

    def insert_user(self, username, password, email, country, age, phone_number):
        self.cursor.execute("insert into user (username, password, email, country, age, phone_number) values (?, ?, ?, ?, ?, ?)",
                            (username, password, email, country, age, phone_number))
        self.connection.commit()

    def login_user(self, username, password):
        user = self.cursor.execute("select * from user where username=? and password=?", (username, password)).fetchone()
        return user

    # def read_all_user(self):
    #     users = self.cursor.execute("select * from user").fetchall()
    #     return users
    #
    # def get_user(self, id):
    #     user = self.cursor.execute("select * from user where id=?", (id,)).fetchone()
    #     return user

    # def update_user(self, id, name, age, address):
    #     self.cursor.execute("update user set name=?, age=?, address=? where id=?",
    #                         (id, name, age, address))
    #     self.connection.commit()

    # def delete_user(self, id):
    #     self.cursor.execute("delete from user where id=?", (id,))
    #     self.connection.commit()


import sqlite3

from utils import hashcode


def con():
    return sqlite3.connect('ddb.db')


def create_table_user():
    conn = con()
    cur = conn.cursor()
    cur.execute("""
        create table if not exists user(
            user_id integer not null primary key autoincrement,
            first_name varchar(30) ,
            last_name varchar(30) ,
            username varchar(30),
            password varchar(30),
            birth_day varchar(30),
            phone_number varchar(13),
            is_admin bool not null default False
        )
    """)
    conn.commit()
    conn.close()


def login_user (username, password):
    password = hashcode(password)

    conn = con()
    cur = conn.cursor()

    query = """
          select user_id from user where username = ? and password = ?
    """
    values = (username, password)
    cur.execute(query, values)

    pk = cur.fetchone()
    conn.close()

    return pk

def register_user (data : dict) :

    conn = con()
    cur = conn.cursor()

    query = """
         insert into user (
            first_name  ,
            last_name  ,
            username ,
            password ,
            birth_day ,
            phone_number 
         )values (? , ? , ? , ? , ? , ?  ) 
    """
    values = (data["first_name"], data["last_name"], data["username"], hashcode(data["password1"]), data["birth_day"], data["phone_number"])
    cur.execute(query, values)

    conn.commit()
    conn.close()

def is_admin(username):
    conn = con()
    cur = conn.cursor()
    query = """
          select is_admin from user where username = ?
    """
    values = (username , )
    cur.execute(query, values)

    pk = cur.fetchone()[0]
    conn.close()
    return pk























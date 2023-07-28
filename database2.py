import sqlite3
from datetime import datetime


def con():
    return sqlite3.connect('ddb.db')

def create_table_kurs():
    conn = con()
    cur = conn.cursor()
    cur.execute("""
           create table kurs(
                kurs_id integer primary key autoincrement,
                name varchar(255),
                summa varchar(50)
           )
    """)
    conn.commit()
    conn.close()

def create_table_users_kurs():
    conn = con()
    cur = conn.cursor()
    cur.execute("""
           create table users_kurs(
                id integer primary key autoincrement,
                user_id integer,
                kurs_id integer,
                datetime varchar(20)
           )
    """)
    conn.commit()
    conn.close()

def admin_enter_kurs():
    conn = con()
    cur = conn.cursor()

    kur_name = input("kursni nomini kiriting : ")
    summa = input("summasini kiriting : ")

    query = """
         insert into kurs(
            name ,
            summa 
         )values(? , ?)
    """
    values = (kur_name, summa)
    cur.execute(query, values)

    conn.commit()
    conn.close()

def kurslar():

    conn = con()
    cur = conn.cursor()

    cur.execute("""
          select * from kurs
    """)
    pk = cur.fetchall()
    for k in pk:
        print (k)

    conn.close()

def kursga_yozilgan_korish():

    conn = con()
    cur = conn.cursor()

    cur.execute("""
          select user_id from user_kurs
    """)
    cd = cur.fetchall()
    for k in cd:
        cur.execute(f"""
             select first_name , last_name , birth_day , phone_number from user where user_id = {k}
        """) 
        malumot = cur.fetchall()
        print (malumot)
    
    conn.close()

def kursga_yozilish(user_id):
    conn = con()
    cur = conn.cursor()
    
    data = datetime(datetime.now())
    kurslar()
    n = input("select kurs id")
    query = """
         insert into user_kurs (
               user_id,
               kurs_id,
               date_time
         )
    """
    values = (user_id, n ,data)
    cur.execute(query, values)

    conn.commit()
    conn.close()

 
def yoz_kur_roy(username):

    conn = con()
    cur = conn.cursor()

    query = """
           select user_id from user where username = ?
    """
    values = (username, )
    cur.execute(query, values)

    pk = cur.fetchone()[0]
    query = """
           select kurs_id from user_kurs where user_id = ?
    """
    values = (pk,)
    cur.execute(query , values)

    cd = cur.fetchall()
    for k in cd:
       cur.execute(f"""
            select name from kurs where user_id = {k}
       """)
       name = cur.fetchall()
       print (name)

    conn.close()

    















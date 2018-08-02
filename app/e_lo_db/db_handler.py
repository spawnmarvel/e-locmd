import sqlite3
from datetime import date, datetime


conn = None
datebase = "e_lo.db"

sql_create_books = "create table if not exists raw_txt(id INTEGER PRIMARY KEY AUTOINCREMENT, title text check(length(title) <= 25) NOT NULL,  note text NOT NULL)"
sql_insert_book = "insert into raw_txt (title, note) values (?, ?)"
sql_select_book = "select * from raw_txt where title = ?"
sql_delete_book = "delete from rax_txt where title = ?"
sql_select_books = "select title from raw_txt"
sql_list_tables = "select name from sqlite_master where type='table'"

def get_conn():
    global conn
    return conn

def get_db():
    global datebase
    return datebase

def init_db_book():
    msg = ""
    try:
        conn = get_conn()
        conn = sqlite3.connect(get_db())
        cur = conn.cursor()
        global sql_create_books
        cur.execute(sql_create_books)
        row = "Created db raw_txt if not exists"
        msg = row
    except sqlite3.OperationalError as e:
        msg = e
    return msg

def get_books():
    msg = ""
    try:
        conn = get_conn()
        conn = sqlite3.connect(get_db())
        cur = conn.cursor()
        global sql_select_books
        cur.execute(sql_select_books)
        row = cur.fetchall()
        msg = row
    except sqlite3.OperationalError as e:
        msg = e
    return msg

def insert_book(title, note):
    msg = ""
    try:
        n_title = str(title)
        n_note = str(note)
        conn = get_conn()
        conn = sqlite3.connect(get_db())
        with conn:
            cur = conn.cursor()
            global sql_insert_book
            cur.execute(sql_insert_book, (n_title, n_note))
            conn.commit()
            row = "Db txt saved"
            msg = row
    except sqlite3.OperationalError as e:
        msg = e
    except sqlite3.IntegrityError as i:
        msg = i
    except Exception as e:
        msg = e
    return msg

def select_book(title):
    msg = ""
    try:
        conn = get_conn()
        conn = sqlite3.connect(get_db())
        cur = conn.cursor()
        global sql_select_book
        cur.execute(sql_select_book, (title,))
        row = cur.fetchone()
        msg = row
    except sqlite3.OperationalError as e:
        msg = e
    return msg

def delete_book(book):
    msg = ""
    try:
        conn = get_conn()
        conn = sqlite3.connect(get_db())
        with conn:
            cur = conn.cursor()
            global sql_delete_book
            cur.execute(sql_delete_book, (book,))
            row = cur.fetchall()
            msg = row
    except sqlite3.OperationalError as e:
        msg = e
    except Exception as e:
        msg = e
    return msg

def list_tables():
    msg = ""
    try:
        conn = get_conn()
        conn = sqlite3.connect(get_db())
        cur = conn.cursor()
        global sql_list_tables
        cur.execute(sql_list_tables)
        row = cur.fetchall()
        msg = row
    except sqlite3.OperationalError as e:
        msg = e
    return msg
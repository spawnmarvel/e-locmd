import sqlite3
from datetime import date, datetime


conn = None
datebase = "e_lo.db"

sql_create_books = "create table if not exists books(id INTEGER PRIMARY KEY AUTOINCREMENT, title text check(length(title) <= 25) NOT NULL,  note text NOT NULL)"
sql_insert_book = "insert into books (title, note) values (?, ?)"
sql_select_book = "select * from books where title = ?"
sql_delete_book = "delete from books where title = ?"
sql_select_books = "select title from books"
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
        row = "Created db books if not exists"
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
    msg = "db insert"
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
            row = "Db book saved"
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
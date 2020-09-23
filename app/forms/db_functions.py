import sqlite3
import datetime
import pandas as pd


# Add a new record
from flask_login import current_user


def add_book(title, price, author_fname, author_lname, app_db_web_location):
    # connect to db
    conn = sqlite3.connect(app_db_web_location)
    print(conn)
    # get timestamp
    curr_timestamp = str(datetime.datetime.now().timestamp())
    # create a cursor
    c = conn.cursor()
    c.execute("INSERT INTO books (title, price, author_fname, author_lname, created_date) "
              "VALUES (?,?,?,?,?)", (title, price, author_fname, author_lname, curr_timestamp))
    conn.commit()
    conn.close()


# Assignment: update the book


# Display all data
def show_all(app_db_web_location):
    # connect to db
    conn = sqlite3.connect(app_db_web_location)
    # create a cursor
    c = conn.cursor()
    c.execute("SELECT * FROM books")
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()
    return items

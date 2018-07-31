from datetime import datetime
import random
from app.e_lo_response import responses
from app.e_lo_db import db_handler
""" Elo is the interface to all functions, a controller. 
    Elo must be generic, since it will be used in Django, only MyCommand will be repalced in Django

"""
class Elo():



    def __init__(self):
        self.name = "e-lo"
        today = datetime.now()
        tmp_born = "2018-07-19 17:57"
        born = datetime.strptime(tmp_born, "%Y-%m-%d %H:%M")
        self.age = today - born
        self.response = None
        self.version = 1.1

    # implemented
    def __repr__(self):
        return repr("<Elo name:" +self.name)
    # implemented
    def toString(self):
        return format(self.name) + ". Age " + format(self.age) + ". V" + format(self.version)
    # implemented, must work on
    def greeting(self): 
        self.response = responses.get_ran_response()
        return self.response
    # implemented, must work on
    def do_math(self): 
        self.response = "Ready for math"
        return self.response
    # implemented, ok
    def get_txt(self, args):
        # 1 = id, 2 = title, 3 = txt
        # print(db_handler.select_book(args))
        return db_handler.select_book(args)
    # implemented, ok
    def get_txt_all(self):
        return db_handler.get_books()
    # implemented, ok
    def insert_txt(self, title, args):
        rv = db_handler.insert_book(title, args)
        return "Saved: " + format(rv)
    # implemented, must work on
    def search_txt(self, book, args):
        todo = args.lower()
        check_book = self.get_txt(book)
        return_book = ""
        rv  = ""
        if check_book == None:
            print("No book with that name: " + return_book)
            return_book = "Not a book"
            rv = return_book
        else:
            # get the title in [1]
            return_book = check_book[1]
            if todo.startswith("nam"):
                rv = "Key search: names from "  + return_book
            elif todo.startswith("pla"):
                rv = "Key search: places from "  + return_book
            elif todo.startswith("plo"):
                rv = "Key search: plot for "  + return_book
            elif todo.startswith("ti"):
                rv = "Key search: time for "  + return_book
            else:
                rv = "Unknown key for " + format(book) + ". Key search: " + format(args) + " type help txt_search"
        return rv
    # not implemented
    def index_txt(self, args):
        return "Indexing book " + format(args) + " to db .....\nbook saved"



    






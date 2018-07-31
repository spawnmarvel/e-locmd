from datetime import datetime
import random
from app.e_lo_response import responses
from e_lo_db import db_handler
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
    def get_book(self, args):
        return db_handler.select_book(args)
    # implemented, ok
    def get_books(self):
        return db_handler.get_books()
    # implemented, ok
    def insert_book(self, title, args):
        rv = db_handler.insert_book(title, args)
        return "Saved: " + format(rv)
    # implemented, must work on
    def search_book(self, book, args):
        todo = args.lower()
        if todo.startswith("nam"):
            return "Key search: names from "  + self.get_book(book)
        elif todo.startswith("pla"):
            return "Key search: places from "  + self.get_book(book)
        elif todo.startswith("plo"):
            return "Key search: plot for "  + self.get_book(book)
        elif todo.startswith("ti"):
            return "Key search: time for "  + self.get_book(book)
        else:
            return "Unknown key for " + format(book) + ". Key search: " + format(args)
    # not implemented
    def index_book(self, args):
        return "Indexing book " + format(args) + " to db .....\nbook saved"



    






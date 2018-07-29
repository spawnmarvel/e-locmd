from datetime import datetime
import random
from app.e_lo_response import responses
from e_lo_db import db_handler

class Elo():



    def __init__(self):
        self.name = "e-lo"
        today = datetime.now()
        tmp_born = "2018-07-19 17:57"
        born = datetime.strptime(tmp_born, "%Y-%m-%d %H:%M")
        self.age = today - born
        self.response = None
        self.version = 1.1

    def __repr__(self):
        return repr("<Elo name:" +self.name)

    def toString(self):
        return format(self.name) + ". Age " + format(self.age) + ". V" + format(self.version)

    def greeting(self): 
        self.response = responses.get_ran_response()
        return self.response
    def do_math(self): 
        self.response = "Ready for math"
        return self.response

    def get_book(self, args):
        return format(args)

    def index_book(self, args):
        return "Indexing book " + format(args) + " to db .....\nbook saved"

    def save_book(self, title, args):
        rv = db_handler.insert_book(title, args)
        return "Saved: " + format(rv)

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



    






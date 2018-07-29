from datetime import datetime
from cmd import Cmd
import os
# e-lo skills
from textblob import TextBlob
from utility import helper
from e_lo_db import db_handler
# e-lo
from app.e_lo import e_lo as cls_elo
elo = cls_elo.Elo()

""" First thing to know about cmd.Cmd: you subclass it and customize the subclass to be your command prompt."""
""" The methods of this subclass that begin with do_ are now your prompt commands """

class MyCommand(Cmd):

    def about(self):
        """ About the app """
        print("***************************************")
        print("Welcome to the chatbot : " + format(elo.toString()))
        print("Type help for commands to use in English., i.e help book_list")
        print("***************************************")

    def do_math(self, args):
        """Teaching and testing you in math"""
        print("Yes, e-lo start math quiz")
        print(elo.do_math())
        # raise SystemExit


    def do_book_get(self, args):
        """Get the book, with title args and shows it on on screen if it exists"""
        if len(args) == 0:
            print("Books saved is:  " + format(db_handler.get_books()) + ". Type book_get title")
        else:
            print("Trying to fetch book> " + format(args))
            rv = db_handler.select_book(args)
            if rv == None:
                print("No book named " + format(args))
            else:
                # print(rv)
                print("***\n" + rv[2] + "\n***")
                # print(db_handler.delete_book(args))

    def do_book_list(self, args):
        """List all the books in app-books, stored the book in args if present and the file exists"""
        try:
            for root, dirs, files in os.walk("./information"):
                for filename in files:
                    print(filename)
                    if len(args) > 0:
                        if filename == args:
                            rv = db_handler.select_book(args)
                            if rv[1] == args:
                                print("Book " + format(rv[1]) + " is already saved")
                            else:
                                note = helper.read_file(filename)
                                print(format(db_handler.insert_book(args, note)))
                            
        except Exception as ex:
            print(ex)

                    

    def do_book_search(self, args):
        """Search a book for :\n["names", "nam", "places", "pla", "plot", "plo", "time", "ti", ]
        \nbook_search hero names"""
        try:
            tmp = args.split(" ")
            book = tmp[0]
            search_word = tmp[1]
        
            if len(book) == 0:
                book = "That is not a book to save"
            else:
                book = book
            print(elo.search_book(book, search_word))

        except IndexError as i:
            print("Invalid params in cmd, type help")

    def do_talk(self, args):
        """Pure random talking"""
        print(elo.greeting())
        # raise SystemExit

    def do_q(self, args):
        """Quits the program, type q"""
        print("Quitting...")
        raise SystemExit
    
    




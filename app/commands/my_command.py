from datetime import datetime
from cmd import Cmd
import os
# e-lo skills
from textblob import TextBlob
from utility import helper
# e-lo
from app.e_lo import e_lo as cls_elo


""" First thing to know about cmd.Cmd: you subclass it and customize the subclass to be your command prompt."""
""" The methods of this subclass that begin with do_ are now your prompt commands """

class MyCommand(Cmd):
    # interface for Elo
    elo = cls_elo.Elo()

    # implemented, ok
    def about(self):
        """ About the app """
        print("***************************************")
        print("Welcome to the chatbot : " + format(MyCommand.elo.toString()))
        print("Type help for commands to use in English., i.e help book_list")
        print("***************************************")
    
    # implemented, must work on
    def do_math(self, args):
        """Teaching and testing you in math"""
        print("Yes, e-lo start math quiz")
        print(self.elo.do_math())

    # implemented, ok
    def do_book_get(self, args):
        """Get the book, with title args and shows it on on screen if it exists"""
        if len(args) == 0:
            print("Books saved is:  " + format(MyCommand.elo.get_books()) + ". Type book_get title")
        else:
            print("Trying to fetch book> " + format(args))
            rv = MyCommand.elo.get_book(args)
            if rv == None:
                print("No book named " + format(args))
            else:
                # print(rv)
                print("***\n" + rv[2] + "\n***")
                # print(db_handler.delete_book(args))

    # implemented, ok
    def do_book_list(self, args):
        """List all the books in app-books, stored the book in args if present and the file exists"""
        try:
            for root, dirs, files in os.walk("./information"):
                for filename in files:
                    print(filename)
                    if len(args) > 0:
                        if filename == args:
                            rv = MyCommand.elo.get_book(args)
                            if rv[1] == args:
                                print("Book " + format(rv[1]) + " is already saved")
                            else:
                                note = helper.read_file(filename)
                                MyCommand.elo.insert_book(args, note)
                   
        except Exception as ex:
            print(ex)
                    
    # implemnented, must work on
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
            print(MyCommand.elo.search_book(book, search_word))
        except IndexError as i:
            print("Invalid params in cmd, type help")

    def do_book_data(self, args):
          """TextBlob functions is used here, book_data title key"""
          try:
              tmp = args.split(" ")
              book = tmp[0]
              key = tmp[1]
              print("Get data for " + book + " key " + key)
              print("Textblob functions")
          except Exception as ex:
              print(ex)

    # implemented, must work on
    def do_talk(self, args):
        """Pure random talking"""
        print(MyCommand.elo.greeting())
       
    # implemented, ok
    def do_q(self, args):
        """Quits the program, type q"""
        print("Quitting...")
        raise SystemExit
    
    




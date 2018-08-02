from datetime import datetime
from cmd import Cmd
import os
# e-lo skills
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
    def do_txt_get(self, args):
        """Get the book, with title args and shows it on on screen if it exists"""
        if len(args) == 0:
            print("Books saved is:  " + format(MyCommand.elo.get_txt_all()) + ". Type book_get title")
        else:
            print("Trying to fetch book> " + format(args))
            rv = MyCommand.elo.get_txt(args)
            if rv == None:
                print("No book named " + format(args))
            else:
                # print(rv)
                print("***\n" + rv[2] + "\n***")
                # print(db_handler.delete_book(args))

    # implemented, ok
    def do_txt_list(self, args):
        """List all the books in app-books, stored the book in args if present and the file exists"""
        try:
            for root, dirs, files in os.walk("./information"):
                for filename in files:
                    print(filename)
                    if len(args) > 0:
                        if filename == args:
                            rv = MyCommand.elo.get_txt(args)
                            # if return from get_text is none, we have not saved the book before
                            if rv != None:
                                if rv[1] == args:
                                    print("Book " + format(rv[1]) + " is already saved")      
                            else:
                                # will not use file reader on django, only db
                                # the book from gte_text is none, w ehave not saved it before
                                print("store file")
                                note = helper.read_file(filename)
                                MyCommand.elo.insert_txt(args, note)
                            
                   
        except Exception as ex:
            print("here \n" + format(ex))
                    
    # implemnented, must work on
    def do_txt_search(self, args):
        """Search a book for :\n["names", "nam", "places", "pla", "plot", "plo", "time", "ti", ]
        \nbook_search hero names"""
        try:
            tmp = args.split(" ")
            book = tmp[0]
            search_word = tmp[1]
            if len(book) == 0:
                book = "That is not a saved book"
            else:
                book = book
                print(MyCommand.elo.search_txt(book, search_word))
        except IndexError as i:
            print("Invalid params in cmd, type help")

    def do_txt_data(self, args):
          """TextBlob functions is used here, book_data title"""
          try:
              book = args
              tmp = MyCommand.elo.data_txt(book)
              name = tmp[0]
              blob = tmp[1]
              noun = tmp[2]
              print(name)
              s = set(noun)
              print("Nouns all " + format(len(noun)) + ", distinct " + format(len(s)))
              print("Nouns\n" + format(s))
              c = 0
              for sen in blob.sentences:
                  print("Sentence " + format(c) + "\n" + format(sen))
                  c += 1
          except Exception as ex:
              print("Please give a valid cmd and select a txt that is saved.\ntxt_data title. Exception:" + format(ex))

    # implemented, must work on
    def do_talk(self, args):
        """Pure random talking"""
        print(MyCommand.elo.greeting())
       
    # implemented, ok
    def do_q(self, args):
        """Quits the program, type q"""
        print("Quitting...")
        raise SystemExit
    
    




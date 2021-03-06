from datetime import datetime
from cmd import Cmd
import os
# e-lo skills
from utility import helper
# e-lo
from app.e_lo import e_lo as cls_elo
from app.e_lo_db import db_handler


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
        print(self.elo.get_math())

    # implemented, ok
    def do_txt_delete(self, args):
        """Delete txt with args"""
        if len(args) > 0:
            rv = MyCommand.elo.get_txt(args)
            if rv == None:
                print("No such txt")
            else:
                print(MyCommand.elo.delete_txt(args))
        else:
            print("Please provide args, and a valid one")

    def do_txt_get(self, args):
        """Get the book, with title args and shows it on on screen if it exists"""
        if len(args) == 0:
            print("Txt saved is:  " + format(MyCommand.elo.get_txt_all()) + ". Type txt_get title")
        else:
            print("Trying to fetch txt> " + format(args))
            rv = MyCommand.elo.get_txt(args)
            if rv == None:
                print("No book named " + format(args))
            else:
                print("Data:")
                print("Title " + format(rv[1]))
                print("Amount of sentences " + format(rv[3]))
                print("Amount of words " + format(rv[4]))
                avg_word_sentences = rv[5]
                if avg_word_sentences > 20:
                    print("Long sentences, avg for word in each sentences " + format(avg_word_sentences))
                else:
                     print("Long sentences, avg for word in each sentences " + format(avg_word_sentences))
                print("Text:")
                print(rv[2])
                # print(db_handler.delete_book("redhood.txt"))

    # implemented, ok
    def do_txt_files(self, args):
        """List all the files stored in ./information/ folder"""
        try:
             for root, dirs, files in os.walk("./information"):
                 for filename in files:
                     print(filename)

        except Exception as ex:
            print(ex)

    def do_txt_index(self, args):
        """List all the txt in folder and stored the txt in args if present and the file exists"""
        file_exist = False
        try:
            if len(args) > 0:
                for root, dirs, files in os.walk("./information"):
                    for filename in files:
                        # print(format(filename) + " =  " + format(args))
                        if filename == args:
                            file_exist = True
                            rv = MyCommand.elo.get_txt(args)
                            # if return from get_text is none, we have not saved the book before
                            if rv != None:
                                if rv[1] == args:
                                    print("txt " + format(rv[1]) + " is already saved")   
                            else:
                                # will not use file reader on django, only db
                                # the book from gte_text is none, w ehave not saved it before
                                print("Storing file....")
                                tu = helper.read_file(filename)
                                text = tu[0]
                                sentences = tu[1]
                                words = tu[2]
                                print(sentences)
                                print(words)
                                print(MyCommand.elo.insert_txt(args, text, sentences, words))
                    if file_exist:
                        pass
                    else:
                        print(format(args) + " does not exist in ./information/ folder ")
            else:
                print("Please provide args and check the txt files in ./information/ folder")
                            
        except Exception as ex:
            print("here \n" + format(ex))
                    
    # implemnented, must work on
    def do_txt_search(self, args):
        """Search a txt for data format for key :\n["names", "nam", "places", "pla", "plot", "plo", "time", "ti", ]
        \ntxt_search hero names"""
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
          """TextBlob functions is used here, txt_data title"""
          try:
              print("add amount of words in file read, store in db")
              book = args
              tmp = MyCommand.elo.data_txt(book)
              name = tmp[0]
              blob = tmp[1]
              noun = tmp[2]
              print(name)
              s = set(noun)
              print("Nouns all " + format(len(noun)) + ", distinct " + format(len(s)))
              print("Nouns original\n" + format(noun))
              c = 0
              for sen in blob.sentences:
                  # print("Sentence " + format(c) + "\n" + format(sen))
                  c += 1
          except Exception as ex:
              print("Please give a valid cmd and select a txt that is saved.\ntxt_data title. Exception:" + format(ex) + "\nSaved is " + format(MyCommand.elo.get_txt_all()))
    
    def do_txt_summary(self, args):
        """TextBlob , txt_summary title"""
        try:
            print("Summary")
            txt = args
            tmp = MyCommand.elo.data_txt(txt)
            data = tmp[3]
            print("Data:")
            print("Title " + format(data[1]))
            print("Amount of sentences " + format(data[3]))
            print("Amount of words " + format(data[4]))
            avg_word_sentences = data[5]
            if avg_word_sentences > 20:
                print("Long sentences, avg for word in each sentences " + format(avg_word_sentences))
            else:
                print("Long sentences, avg for word in each sentences " + format(avg_word_sentences))
            print("Text:")

            blob = tmp[1]
            nouns = set()
            for word, tag in blob.tags:
                # print(tag)
                if tag == "NN":
                    nouns.add(word.lemmatize())
            print("This text is about:")
            c = 0
            rv = ""
            for w in nouns:
                if c == 5:
                    rv += w.pluralize() + "\n"
                    c = 0
                else:
                    
                    rv += " " + w.pluralize()
            print(rv)

        except Exception as ex:
            print(ex)

    # implemented, must work on
    def do_talk(self, args):
        """Pure random talking or talk about all that is fed to e-elo"""
        print(MyCommand.elo.greeting())
       
    # implemented, ok
    def do_q(self, args):
        """Quits the program, type q"""
        print("Quitting...")
        raise SystemExit
    
    




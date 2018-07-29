from app.commands import my_command
from app.e_lo_db import db_handler

def prerequisite_app():
    print("***************************************")
    print("Prerequisite:")
    print(db_handler.init_db_book())
    print("Tables in db:")
    print(db_handler.list_tables())
    print("***************************************")

if __name__ == "__main__":
   
    prerequisite_app()
    # cmd's
    my_cmd = my_command.MyCommand()
    my_cmd.prompt = ">"
    my_cmd.cmdloop(my_cmd.about())
    
#!/usr/bin/python3
"""this is the console for AirBnB"""

import cmd
import re
from shlex import split


def divider(arg):
    square = re.search(r"\[(.*?)\]", arg)
    curly = re.search(r"\{(.*?)\}", arg)

    if curly is None:
        if square is None:
            return [i.strip(",") for i in split(arg)]
        else:
            before = split(arg[:square.span()[0]])
            total = [i.strip(",") for i in before]
            total.append(square.group())
            return total
    else:
        before = split(arg[:curly.span()[0]])
        total = [i.strip(",") for i in before]
        total.append(curly.group())
        return total
            

class HBNBCommand(cmd.Cmd):
    """ Defines the BnB command of the ALX holberton shell like command.
    Attributes:
        prompt (str): The place where user inputs.
    """

    prompt = "(hbnb) "
    ourclasses = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
            }



    def emptyline(self):
        """this is produced when the line is empty"""
        pass
    def do_quit(self, arg):
        """ this quits the whole shell command"""
        return True
    def do_EOF(self, arg):
        """this is done when a file is ended in shell"""
        print("")
        return True
    def do_create(self, arg):
        """ this creates a new instance model for the project"""
        argl = divider(arg)
        if len(argl) == 0:
            print("** class name is missing **")
        elif argl[0] not in HBNBCommand.ourclasses:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):
        """this is to show the model"""
        print("i am showing my nigger")
    def do_destroy(self, arg):
        """this is to destroy the model"""
        print("i am destroying")
    def do_all(self, arg):
        """this is to display all classes of model"""
        print("all is all brother")
    def do_count(self, arg):
        """this counts your model"""
        print(" i am counting it brother")
    def do_update(self, arg):
        """this update your model to new model"""
        print("i am updating brother")


if __name__ == "__main__":
    HBNBCommand().cmdloop()

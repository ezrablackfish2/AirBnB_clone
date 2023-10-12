#!/usr/bin/python3
"""this is the totality of console for our AirBnB clone"""
import cmd
import re
from shlex import split


def divider(arg):
    curly = re.search(r"\{(.*?)\}", arg)
    square = re.search(r"\[(.*?)\]", arg)
    if curly is None:
        if square is None:
            return [j.strip(",") for j in split(arg)]
        else:
            before = split(arg[:sqaure.span()[0]])
            total = [j.strip(",") for j in before]
            total.append(square.group())
            return total
    else:
        before = split(arg[:curly.span()[0]])
        total = [j.strip(",") for j in before]
        total.append(curly.group())
        return total

class HBNBCommand(cmd.Cmd):
    """this is our AirBnB clone main workstation.
    Attributes:
        prompt (str): the input the user inserts prompt.
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

    def do_author(self, arg):
        """ this shows who made the console"""
        print("ezra and aman did the console")

    def emptyline(self):
        """this is done if the user just inputs enter only."""
        pass

    def default(self, arg):
        """if the user inserts something other than the usual words."""
        cmds = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        dat = re.search(r"\.", arg)
        if dat is not None:
            token = [arg[:dat.span()[0]], arg[dat.span()[1]:]]
            dat = re.search(r"\((.*?)\)", token[1])
            if dat is not None:
                cmd = [token[1][:dat.span()[0]], dat.group()[1:-1]]
                if cmd[0] in cmds.keys():
                    caller = "{} {}".format(token[0], cmd[1])
                    return cmds[cmd[0]](caller)
        print("*** Unknown syntax: {}".format(arg))
        return False


    def do_quit(self, arg):
        """exits the console."""
        return True

    def do_EOF(self, arg):
        """if a file was inserted this is when the file ends."""
        print("")
        return True
    def do_hi(self, arg):
        """this just says hi"""
        print("Hi everyone i am the AirBnB clone how can i help you")

    def do_create(self, arg):
        """this is used to create a new instance of already known class."""
        token = divider(arg)
        if len(token) == 0:
            print("** class name missing **")
        elif token[0] not in HBNBCommand.ourclasses:
            print("** class doesn't exist **")
        else:
            print(eval(token[0])().id)
            storage.save()

    def do_guide(self, arg):
        """ this guides the user """
        print("this guides the user to the ultimate peak of humanity wait")

    def do_show(self, arg):
        """this is used to show a classes one attribute with you specifying it."""
        token = divider(arg)
        data = storage.all()
        if len(token) == 0:
            print("** class name missing **")
        elif token[0] not in HBNBCommand.ourclasses:
            print("** class doesn't exist **")
        elif len(token) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(token[0], token[1]) not in data:
            print("** no instance found **")
        else:
            print(data["{}.{}".format(token[0], token[1])])

    def do_pushup(self, arg):
        """this does push up"""
        print("push up 1 push up 2push up 3 ...")

    def do_destroy(self, arg):
        """this is used to destroy a class."""
        token = divider(arg)
        data = storage.all()
        if len(token) == 0:
            print("** class name missing **")
        elif token[0] not in HBNBCommand.ourclasses:
            print("** class doesn't exist **")
        elif len(token) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(token[0], token[1]) not in data.keys():
            print("** no instance found **")
        else:
            del data["{}.{}".format(token[0], token[1])]
            storage.save()

    def do_all(self, arg):
        """to list everything in the json file."""
        token = divider(arg)
        if len(token) > 0 and token[0] not in HBNBCommand.ourclasses:
            print("** class doesn't exist **")
        else:
            dataarray = []
            for data in storage.all().values():
                if len(token) > 0 and token[0] == data.__class__.__name__:
                    dataarray.append(data.__str__())
                elif len(token) == 0:
                    dataarray.append(data.__str__())
            print(dataarray)

    def do_count(self, arg):
        """Usage: retrieve the number of attributes in one class."""
        token = divider(arg)
        count = 0
        for data in storage.all().values():
            if token[0] == data.__class__.__name__:
                count += 1
        print(count)
    def do_bye(self, arg):
        """this says goodbye to the user"""
        print("good bye!")

    def do_update(self, arg):
        """this updates an attribute of one class with you telling it."""
        
        token = divider(arg)
        data = storage.all()

        if len(token) == 0:
            print("** class name missing **")
            return False
        if token[0] not in HBNBCommand.ourclasses:
            print("** class doesn't exist **")
            return False
        if len(token) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(token[0], token[1]) not in data.keys():
            print("** no instance found **")
            return False
        if len(token) == 2:
            print("** attribute name missing **")
            return False
        if len(token) == 3:
            try:
                type(eval(token[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(token) == 4:
            info = data["{}.{}".format(token[0], token[1])]
            if token[2] in info.__class__.__dict__.keys():
                valtype = type(info.__class__.__dict__[argl[2]])
                info.__dict__[token[2]] = valtype(token[3])
            else:
                info.__dict__[token[2]] = token[3]
        elif type(eval(token[2])) == dict:
            info = data["{}.{}".format(token[0], token[1])]
            for a, b in eval(token[2]).items():
                if (a in info.__class__.__dict__.keys() and
                        type(info.__class__.__dict__[a]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[a])
                    info.__dict__[a] = valtype(b)
                else:
                    info.__dict__[a] = b
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

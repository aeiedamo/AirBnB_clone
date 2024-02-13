#!/usr/bin/python3
"""This files runs a console program"""
import cmd
import json
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.city import City
from models.place import Place

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Amenity": Amenity,
    "State": State,
    "Review": Review,
    "City": City,
    "Place": Place,
}


class HBNBCommand(cmd.Cmd):
    """This defines properties of HBNBCommand class"""

    prompt = "(hbtn) "

    def do_EOF(self, line):
        """send EOF signal to quit program"""
        print()
        return True

    def help_EOF(self):
        """to help when sending an EOF File"""
        print("EOF signal to exit the program")
        print()

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """to help when entering quit"""
        print("Quit command to exit the program")
        print()

    def postloop(self):
        """after the loop ends"""
        print()

    def do_create(self, arg):
        """to create an object of a class"""
        args = arg.split()
        if not checkClass(args):
            return
        newObj = classes[args[0]]()
        newObj.save()
        print(newObj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based
        on the class name and id"""
        args = arg.split()
        if not checkClass(args, True):
            return
        objects = storage.all()
        key = "{}.{}".format(args[0], args[1])
        to_show = objects.get(key)
        if to_show is None:
            print("** no instance found **")
            return
        print(to_show)

    def do_destroy(self, arg):
        """to delete/destroy an object"""
        args = arg.split()
        if not checkClass(args, True):
            return
        objects = storage.all()
        key = "{}.{}".format(args[0], args[1])
        to_destroy = objects.get(key)
        if to_destroy is None:
            print("** no instance found **")
            return
        del objects[key]
        storage.save()

    def do_all(self, arg):
        """to print all objects stored"""
        args = arg.split()
        objects = storage.all()
        if len(args) < 1:
            print(["{}".format(str(v)) for k, v in objects.items()])
            return
        if not checkClass(args):
            return
        print(
            [
                "{}".format(str(v))
                for k, v in objects.items()
                if type(v).__name__ == args[0]
            ]
        )

    def do_update(self, arg):
        """to update an object values"""
        args = arg.split(maxsplit=3)
        if not checkClass(args, True):
            return
        objects = storage.all()
        key = "{}.{}".format(args[0], args[1])
        to_update = objects.get(key)
        if to_update is None:
            print("** no instance found **")
            return
        match_json = re.findall(r"{.*}", arg)
        if match_json:
            payload = json.loads(match_json[0])
            for k, v in payload.items():
                setattr(to_update, k, v)
            storage.save()
            return
        if not checkAttr(args):
            return
        first = re.findall(r"^[\"\'](.*?)[\"\']", args[3])
        if first:
            setattr(to_update, args[2], first[0])
        else:
            value = args[3].split()
            setattr(to_update, args[2], parseStr(value[0]))
        storage.save()


def checkClass(args, flag=False):
    """to check if a class exists"""
    if len(args) < 1:
        print("** class name missing **")
        return False
    if args[0] not in classes.keys():
        print("** class doesn't exist **")
        return False
    if len(args) < 2 and flag:
        print("** instance id missing **")
        return False
    return True


def checkAttr(args):
    """to check if attributes are valid"""
    if len(args) < 3:
        print("** attribute name missing **")
        return False
    if len(args) < 4:
        print("** value missing **")
        return False
    return True


def parseStr(arg):
    """parse arg to its type"""
    parsed = re.sub('"', "", arg)

    if isinstance(parsed, int):
        return int(parsed)
    elif isinstance(parsed, float):
        return float(parsed)
    return arg


if __name__ == "__main__":
    HBNBCommand().cmdloop()

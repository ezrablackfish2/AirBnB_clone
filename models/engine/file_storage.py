#!/usr/bin/python3
"""this is the json file storage system."""
import json


class FileStorage:
    """this is the json editing class.

    Attributes:
        path (str): The name of the file to save objects to.
        infos (dict): A dictionary of instantiated objects.
    """
    path = "file.json"
    infos = {}

    def all(self):
        """Returnallall values of a class."""
        return FileStorage.infos

    def new(self, obj):
        """create new class for an object"""
        classname = obj.__class__.__name__
        FileStorage.infos["{}.{}".format(classname, obj.id)] = obj

    def save(self):
        """this dumps or saves data to JSON."""
        info = FileStorage.infos
        data = {obj: info[obj].to_dict() for obj in info.keys()}
        with open(FileStorage.path, "w") as f:
            json.dump(data, f)

    def reload(self):
        """extracts data frm json dump."""
        try:
            with open(FileStorage.__file_path) as f:
                data = json.load(f)
                for o in data.values():
                    classname = o["__class__"]
                    del o["__class__"]
                    self.new(eval(classname)(**o))
        except FileNotFoundError:
            return

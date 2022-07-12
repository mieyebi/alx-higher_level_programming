#!/usr/bin/python3
"""A class Base with a folder named models"""
import json
import csv


class Base:
    """A class base with class attributes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the class base"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a json string representation"""
        if list_dictionaries == None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes a string represetation to a file"""
        fl = cls.__name__ + ".json"
        with open(fl, "w", encoding="utf-8") as jfile:
            if list_objs == None:
                jfile.write("[]")
            else:
                list_dicts = [a.to_dictionary() for a in list_objs]
                jfile.write(Base.to_json_string(list_dicts))

    @classmethod
    def from_json_string(json_string):
        """returns the list of the json string representation"""
        if json_strinf == None or json_string == "[]":
            return []
        return json.loads(json_string)


    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all sttributes set"""
        if "Rectangle" in f"{cls.__dict__['__init__']}":
            inst = cls(10, 10)
            inst.update(**dictionary)
            return inst
        elif "Square" in f"{cls.__dict__['__init__']}":
            inst = cls(10, 10, 10, 10)
            inst.update(**dictionary)
            return inst

    @classmethod
    def load_from_file(cls):
        """returns a python list of instances"""
        if "Rectangle" in f"{cls.__dict__['__init__']}":
            file_name = "Rectangle.json"
        elif "Square" in f"{cls.__dict__['__init__']}":
            file_name = "Square.json"

        obj_list = []
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                lst = cls.from_json_string(f.read())
                obj_list += [cls.create(**objct) for objct in lst]
                return obj_list
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes to csv"""
        if "Rectangle" in f"{cls.__dict__['__init__']}":
            file_name = "Rectangle.csv"
            with open(file_name, "w", encoding="utf-8") as f:
                tpl = [list((itm.id, itm.width, itm.height,
                             itm.x, itm.y)) for itm in list_objs]
                writer = csv.writer(f)
                for item in tpl:
                    writer.writerow(item)
        elif "Square" in f"{cls.__dict__['__init__']}":
            file_name = "Square.csv"
            with open(file_name, "w", encoding="utf-8") as f:
                tpl = [list((itm.id, itm.size, itm.x,
                             itm.y)) for itm in list_objs]
                writer = csv.writer(f)
                for item in tpl:
                    writer.writerow(item)

    @classmethod
    def load_from_file_csv(cls):
        """deserializes from csv"""
        if "Rectangle" in f"{cls.__dict__['__init__']}":
            file_name = "Rectangle.csv"
            with open(file_name, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                list_of_objs = list(reader)
                lst = []
                for item in list_of_objs:
                    item = [int(itm) for itm in item]
                    args = tuple(item)
                    # objct = cls(*args)
                    objct = cls(id=item[0], width=item[1],
                                height=item[2], x=item[3],
                                y=item[4])
                    lst.append(objct)
                return lst
        elif "Square" in f"{cls.__dict__['__init__']}":
            file_name = "Square.csv"
            with open(file_name, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                list_of_objs = list(reader)
                lst = []
                for item in list_of_objs:
                    item = [int(itm) for itm in item]
                    args = tuple(item)
                    # objct = cls(*args)
                    objct = cls(id=item[0], size=item[1],
                                x=item[2], y=item[3])
                    lst.append(objct)
                return lst

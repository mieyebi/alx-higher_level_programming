#!/usr/bin/python3
"""a class Square that inherits from the Rectangle class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """a class square that inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes the attributes of the square"""
        super().__init__(size, size, x, y, id)


    @property
    def size(self):
        """setting the width of the rectangle"""
        return self.__width

    @size.setter
    def size(self, value):
        self.__width = value
        self.__height = value


    def update(self, *args, **kwargs):
        """assigns arguments to each attribute"""
        if len(args) != 0:
            i = 0
            for a in args:
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.size = a
                elif i == 2:
                     self.size = a
                elif i == 3:
                     self.x = a
                elif i == 4:
                     self.y = a
                i += 1

        else:
            for a in kwargs:
                if a == "id":
                    self.id = kwargs[a]
                elif a == "size":
                    self.size = kwargs[a]
                elif a == "size":
                    self.size = kwargs[a]
                elif a == "x":
                    self.x = kwargs[a]
                elif a == "y":
                    self.y = kwargs[a]

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

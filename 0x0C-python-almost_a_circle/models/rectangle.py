#!/usr/bin/python3
"""a class Rectangle that inherits from the class Base"""
import json
from models.base import Base


class Rectangle(Base):
    """A subclass rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """defines and initializes the rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """setting the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """setting the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """setting x of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """setting the height of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the rectangle instance"""
        area = self.width * self.height
        return area

    def display(self):
        """prints # to the stdout representing the rectangle instance"""
        if self.width <= 0 or self.height <= 0:
            print("")
            return

        for x in range(self.x):
            print("", end="")
        for y in range(self.y):
            print("")
        for h in range(self.height):
            for w in range(self.width):
                print("#", end="")
            print("")


    def update(self, *args, **kwargs):
        """assigns arguments to each attribute"""
        if len(args) != 0:
            i = 0
            for a in args:
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.width = a
                elif i == 2:
                     self.height = a
                elif i == 3:
                     self.x = a
                elif i == 4:
                     self.y = a
                i += 1

        else:
            for a in kwargs:
                if a == "id":
                    self.id = kwargs[a]
                elif a == "width":
                    self.width = kwargs[a]
                elif a == "height":
                    self.height = kwargs[a]
                elif a == "x":
                    self.x = kwargs[a]
                elif a == "y":
                    self.y = kwargs[a]


    def to_dictionary(self):
        """dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """string representation of the rectangle"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id, self.x, self.y, self.width, self.height)

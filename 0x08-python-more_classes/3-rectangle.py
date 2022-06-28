#!/usr/bin/python3
"""creates a class and defines it"""

class Rectangle:
    """defines the class rectangle"""

    def __init__(self, width=0, height=0):
        """defines the rectangle attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """sets the property of the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """the width setter"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """defines the height to be set"""
        return self.__height

    @height.setter
    def height(self, height):
        """defines the set height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer""")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.height * self.width

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.width is 0:
            return 0
        elif self.height is 0:
            return 0
        else:
            return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """using strings"""
        if self.width == 0:
            return ""
        if self.height == 0:
            return ""
        a = self.width * "#"
        b = ""

        for i in range(self.height):
            b += a
            if i != self.height - 1:
                b += "\n"

        return b

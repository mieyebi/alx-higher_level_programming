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
        def width(self, value):
            """the width setter"""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__value = value

    @property
        """setting the decorator property for height"""
        def height(self):
            """defines the height to be set"""
            return self.__height

    @height.setter
        """sets the height"""
        def height(self, value):
            """defines the set height"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer""")
            if value < 0:
                raise ValueError("height must be >= 0""")
            self.__value = value

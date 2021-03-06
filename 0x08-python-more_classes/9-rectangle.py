#!/usr/bin/python3
"""creates a class and defines it"""

class Rectangle:
    """defines the class rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    @classmethod
    def square(cls, size=0):
        """returns a square as the a new rectangle instance"""
        new = Rectangle(size, size)
        return new


    def __init__(self, width=0, height=0):
        """defines the rectangle attributes"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1
        self.print_symbol = None

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
            raise ValueError("height must be >= 0""")
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.height * self.width

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.width == 0:
            return 0
        elif self.height == 0:
            return 0
        else:
            return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """using strings"""
        if self.width == 0:
            return ""
        if self.height == 0:
            return ""
        if self.print_symbol is None:
            self.print_symbol = str(type(self).print_symbol)
        else:
            self.print_symbol = str(self.print_symbol)
        a = self.width * self.print_symbol
        b = ""

        for i in range(self.height):
            b += a
            if i != self.height - 1:
                b += "\n"

        return b

    def __repr__(self):
        """represents the object"""
        return "Rectangle({}, {})".format(self.width, self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compares rectangles for equality"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __del__(self):
        """deletes rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

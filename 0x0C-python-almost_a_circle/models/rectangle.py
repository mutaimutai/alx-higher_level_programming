#!/usr/bin/python3
"""Here we need to write a module for a class rectangle"""
from models.base import Base
"""Defining a class rectangle """


class Rectangle(Base):
    """Thi is the blueprint of the rectangle class that inherits from base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Creating an object of the rectangle class
        Args:
            width (int):This is the width of the rectangle
            height (int):Height of the rectangle
            x (int): X-coordinate of the rectangle (default is 0)
            y (int): Y-coordinate of the rectangle (default is 0)
            id (int): The object id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        

    @property
    def width(self):
        """
        Get the width of the rectangle
        Returns:
            int: the width of the rectangle
            """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle
        Args:
            value: The value to set as width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value


    @property
    def height(self):
        """
        Get the height of the rectangle
        Returns:
            int: the height of the rectangle
            """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle
        Args:
            value: The value to set as height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Get the X-coordinate of the rectangle (default is 0)
        Returns:
            int: the X-coordinate of the rectangle
            """
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the X-coordinate of the rectangle
        Args:
            value: The value to set as X-coordinate
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value


    @property
    def y(self):
        """
        Get the Y-coordinate of the rectangle (default is 0)
        Returns:
            int: the Y-coordinate of the rectangle
            """
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the Y-coordinate of the rectangle
        Args:
            value: The value to set as Y-coordinate
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Finding the are of the rectangle"""
        area = self.__width * self.__height
        return area

    def display(self):
        """Displays the rectangle using '#' to the standard output"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """We have overriden the str method to print info about an object"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args):
        """This function updates the attributes of an object
        Args:
            args:This are arguments to be updated
        """
        count = len(args)
        if count >= 1:
            self.id = args[0]
        if count >= 2:
            self.width = args[1]
        if count >= 3:
            self.height = args[2]
        if count >= 4:
            self.x = args[3]
        if count >= 5:
            self.y = args[4]

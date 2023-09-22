#!/usr/bin/python3
"""Here we need to write a module for a class rectangle."""
from models.base import Base


class Rectangle(Base):
    """Thi is the blueprint of the rectangle class inherits Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Creating an object of the rectangle class.
            Args:
                width (int):This is the width of the rectangle.
                height (int):Height of the rectangle.
                x (int): X-coordinate of the rectangle (default is 0).
                y (int): Y-coordinate of the rectangle (default is 0).
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
            Get the width of the rectangle.
            Returns:
                int: the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.
            Args:
                value: The value to set as width.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
            Get the height of the rectangle.
            Returns:
                int: the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.
            Args:
                value: The value to set as height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
            Get the X-coordinate of the rectangle (default is 0).
            Returns:
                int: the X-coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the X-coordinate of the rectangle.
            Args:
                value: The value to set as X-coordinate.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
            Get the Y-coordinate of the rectangle (default is 0).
            Returns:
                int: the Y-coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the Y-coordinate of the rectangle.
            Args:
                value: The value to set as Y-coordinate.
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
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
            Assigning key/value arguments to the attributes.
            in my object.
            kwargs is skipped if args is not empty.
            Args:
                *args - variable number of arguments passed.
                **kwargs - keyworded arguments.
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                setattr(self, key, val)
            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """A method that a dictionary representation of an object"""
        return {'x': getattr(self, "x"), 'y': getattr(self, "y"),
                'id': getattr(self, "id"), 'height': getattr(self, "height"),
                'width': getattr(self, "width")}

#!/usr/bin/python3
"""Class rectangle that inherits from Base"""
from .base import Base


class Rectangle(Base):
    """Defining the class Rectangle which inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing an instance of the rectangle class
        Args:
            width (int): Width of the rectangle
            height (int) : Height of the rectangle
            x (int) : The X-coordinate of the rectangle
            y (int) : The Y-coordinate of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of width
        Args:
            value (int) : value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of height
        Args:
            value (int) : value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the X-coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the value of X-coordinate
        Args:
            value (int) : value of X-coordinate
        """
        if not isinstance(value, int):
            raise TypeError("x  must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the Y-coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the value of the Y-coordinate
        Args:
            value (int) : value of the Y-coordinate
        """
        if not isinstance(value, int):
            raise TypeError("y  must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Printing the rectangle instance with character"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """Prints a string representation of a rectangle instance"""
        return (f"[Rectangle] ({self.id})
                {self.x}/{self.y} - {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """
            assigns key/value argument to attributes
            kwargs is skipped if args is not empty
            Args:
                *args -  variable number of no-keyword args
                **kwargs - variable number of keyworded args
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
        """Return the dictionary representation of a rectangle instance"""
        return ({'id': getattr(self,'id'), 'width': getattr(self, 'width'),
                 'height': getattr(self, 'height'), 'x': getattr(self, 'x'),
                 'y': getattr(self, 'y')})

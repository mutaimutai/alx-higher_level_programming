#!/usr/bin/python3
"""
    contains class square that implements class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This is a class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """
           Initializing an oject of the square class
           Args:
               size (int): the size of the sides of th e square
               x (int) : The X-coordinate of the square (default is 0)
               y (int) : The Y-coordinate of the square default is 0)
               id (int) : The object identifier
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size of the square"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

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
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def __str__(self):
        """Overiding the str method"""
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    def to_dictionary(self):
        """This method returns a dictionary representation of a Square"""
        return ({'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y})

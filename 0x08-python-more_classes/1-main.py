#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)
myrectangle = Rectangle(2, -3) 
print(myrectangle.__dict__)

myrectangle.width = 10
myrectangle.height = 3
print(myrectangle.__dict__)

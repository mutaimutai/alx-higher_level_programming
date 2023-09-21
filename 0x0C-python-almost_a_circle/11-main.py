#!/usr/bin/python3
""" 11-main """
from models.square import Square

if __name__ == "__main__":
    s1=Square(1,1,1,1)
    print(f"width =  {s1.width}")
    print(f"size = {s1.size}")
    print(f"x = {s1.x}")
    print(f'y = {s1.y}')
    print("-------------")
    s1.update(2,2,2,2)
    print(f"width =  {s1.width}")
    print(f"size = {s1.size}")
    print(f"x = {s1.x}")
    print(f'y = {s1.y}')
    print("-------------")
    s1.update(size=3,id=3,x=3,y=3)
    print(f"width =  {s1.width}")
    print(f"size = {s1.size}")
    print(f"x = {s1.x}")
    print(f'y = {s1.y}')

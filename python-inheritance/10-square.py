#!/usr/bin/python3
"""Task 10"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Task 10"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

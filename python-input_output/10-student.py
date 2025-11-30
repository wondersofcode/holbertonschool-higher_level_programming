#!/usr/bin/python3
"""Task 10"""


class Student:
    """Task 10"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return dict(self.__dict__)

        result = {}
        for i in attrs:
            if i in self.__dict__:
                result[i] = self.__dict__[i]
        return result

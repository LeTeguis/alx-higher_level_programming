#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""0-square
"""


class Square:
    """Square
    """
    __size = 0
    __position = (0, 0)

    def __init__(self, size=0, position=(0, 0)):
        """
        Note:
            do not include self parameter
        Args:
            size (int): size of Square
            position (tuple): 2 elements
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

    def area(self):
        """
        Note:
            none
        """
        return self.__size * self.__size

    @property
    def size(self):
        """int: getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """int: setter
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        Note: print the graphics square
        """
        if self.__size > 0:
            for i in range(self.__size):
                if self.__position[1] <= self.__position[0]:
                    p = " " * self.__position[0]
                    s = "#" * self.__size
                    print("{}{}".format(p, s))
                else:
                    print("{}".format("#" * self.__size))
        else:
            print()

    @property
    def position(self):
        """tuple: getter
        Note: nothing
        """
        return self.__position

    @position.setter
    def position(self, value):
        """tuple: setter
        Note: Nothing
        """
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

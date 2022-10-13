#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""0-square
"""


class Square:
    """Square
    """
    __size = 0

    def __init__(self, size=0):
        """
        Note:
            do not include self parameter
        Args:
            size (int): size of Square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Note:
            none
        """
        return self.__size * self.__size

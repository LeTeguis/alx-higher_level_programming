#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""singly_linked_list
"""


class Node:
    """Node
    """
    __data = 0
    __next_node = None

    def __init__(self, data, next_node=None):
        """
        Args:
            data (int):
            next_node (Node):
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """int: getter
        """
        return self.__data

    @data.setter
    def data(self, value):
        """int: setter
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Node: getter
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Node: setter
        """
        if value != None and type(value) != Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """SinglyLinkedList
    """
    __head = None

    def __init__(self):
        """
        """
        self.__head = None

    def __str__(self):
        """
        """
        result = ""
        if self.__head != None:
            tmp = self.__head
            while tmp != None:
                if result == "":
                    result = f"{tmp.data}"
                else:
                    result = f"{result}\n{tmp.data}"
                tmp = tmp.next_node
        return result

    def sorted_insert(self, value):
        """
        """
        new_node = Node(value)
        if self.__head == None:
            self.__head = new_node
        else:
            if self.__head.data > value:
                new_node.next_node = self.__head
                self.__head = new_node
            else:
                prev = self.__head
                tmp = prev.next_node
                while tmp != None:
                    if tmp.data > value:
                        break
                    prev = tmp
                    tmp = tmp.next_node
                prev.next_node = new_node
                new_node.next_node = tmp

#!/usr/bin/python3

"""
1-my_list: module
"""


class MyList(list):
    """
    MyList: the chield of list class
    """

    def print_sorted(self):
        """
        print list in sorted
        """
        liste = self.copy()
        i = 0
        j = 0
        for i in range(len(liste) - 1):
            for j in range(i, len(liste)):
                if liste[i] > liste[j]:
                    e = liste[i]
                    liste[i] = liste[j]
                    liste[j] = e
        print(liste)

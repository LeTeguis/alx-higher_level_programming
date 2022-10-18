#!/usr/bin/python3

def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    first = 0
    last = 0
    space = 0
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            if text[last] != ' ':
                space = last
            print(text[first:space + 1])
            print()
            last = i + 1
            first = last
            space = last
        else:
            if text[i] == ' ':
                if text[first] == ' ':
                    last = i + 1
                    first = last
                    space = last
                else:
                    last = i
            else:
                space = i
                last = i
    if text[last] != ' ':
        space = last
    if first < space:
        print(text[first:space + 1], end="")

#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    Units = {"IX": 9, "VIII": 8, "VII": 7, "VI": 6, "V": 5, "IV": 4, "III": 3, "II": 2, "I": 1}
    Tens = {"XC": 90, "LXXX": 80, "LXX": 70, "LX": 60, "L": 50, "XL": 40, "XXX": 30, "XX": 20, "X": 10}
    Hundreds = {"CM": 900, "DCCC": 800, "DCC": 700, "DC": 600, "D": 500, "CD": 400, "CCC": 300, "CC": 200, "C": 100}
    Thousands = {"MMM": 3000, "MM": 2000, "M": 1000}
    resume = {"Units": Units, "Tens": Tens, "Hundreds": Hundreds, "Thousands": Thousands}
    rs = ""
    for e in roman_string:
        rs = f"{rs}{e}"
    valeur = 0
    for k1, v1 in resume.items():
        for k, v in v1.items():
            if k in rs:
                valeur = valeur + v
                rs = rs.replace(k, '*')
                break
    return valeur

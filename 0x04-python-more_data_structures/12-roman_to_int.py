#!/usr/bin/python3

def int_to_roman(valeur):
    if valeur is None or type(valeur) is not int:
        return '0'
    U = ["IX", "VIII", "VII", "VI", "V", "IV", "III", "II", "I"]
    T = ["XC", "LXXX", "LXX", "LX", "L", "XL", "XXX", "XX", "X"]
    H = ["CM", "DCCC", "DCC", "DC", "D", "CD", "CCC", "CC", "C"]
    TH = ["MMM", "MM", "M"]
    G = [U, T, H, TH]

    result = ''
    if valeur == 0:
        result = '0'
    else:
        i = 0
        while valeur != 0:
            p = (9 if i != 3 else 3) - valeur % 10
            if p != 9:
                v = G[i][p]
                result = f"{v}{result}"
            valeur = int(valeur / 10)
            i += 1
    return result


ROMAN_INT = {int_to_roman(i): i for i in range(3999)}


def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    if not roman_string.isupper():
        return 0
    V = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    U = ["IX", "VIII", "VII", "VI", "V", "IV", "III", "II", "I"]
    T = ["XC", "LXXX", "LXX", "LX", "L", "XL", "XXX", "XX", "X"]
    H = ["CM", "DCCC", "DCC", "DC", "D", "CD", "CCC", "CC", "C"]
    TH = ["MMM", "MM", "M"]
    Units = {U[i]: V[i] for i in range(9)}
    Tens = {T[i]: V[i] * 10 for i in range(9)}
    Hundreds = {H[i]: V[i] * 100 for i in range(9)}
    Thousands = {TH[i]: V[6 + i] * 1000 for i in range(3)}
    resume = [Units, Tens, Hundreds, Thousands]
    rs = ""
    for e in roman_string:
        rs = f"{rs}{e}"
    valeur = 0
    for dom in resume:
        for k, v in dom.items():
            if k in rs:
                if k == "V" and "IV" in rs:
                    valeur = valeur + 4
                    k = "IV"
                elif k == "L" and "XL" in rs:
                    valeur = valeur + 40
                    k = "XL"
                elif k == "D" and "CD" in rs:
                    valeur = valeur + 400
                    k = "CD"
                else:
                    valeur = valeur + v
                rs = rs.replace(k, "", 1)
                break
    return valeur

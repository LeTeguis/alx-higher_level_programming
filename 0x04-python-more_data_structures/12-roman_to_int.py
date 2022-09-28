#!/usr/bin/python3

U = ["IX", "VIII", "VII", "VI", "V", "IV", "III", "II", "I"]
T = ["XC", "LXXX", "LXX", "LX", "L", "XL", "XXX", "XX", "X"]
H = ["CM", "DCCC", "DCC", "DC", "D", "CD", "CCC", "CC", "C"]
TH = ["MMM", "MM", "M"]
Units = {U[i]: (9 - i) for i in range(9)}
Tens = {T[i]: (9 - i) * 10 for i in range(9)}
Hundreds = {H[i]: (9 - i) * 100 for i in range(9)}
Thousands = {TH[i]: (3 - i) * 1000 for i in range(3)}
GIR = [U, T, H, TH]
GRI = [Units, Tens, Hundreds, Thousands]


def int_to_roman(valeur):
    if valeur is None or type(valeur) is not int:
        return '0'
    result = ''
    if valeur == 0:
        result = '0'
    else:
        i = 0
        while valeur != 0:
            p = (9 if i != 3 else 3) - valeur % 10
            if p != 9:
                v = GIR[i][p]
                result = f"{v}{result}"
            valeur = int(valeur / 10)
            i += 1
    return result


def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    if not roman_string.isupper():
        return 0
    rs = ""
    for e in roman_string:
        rs = f"{rs}{e}"
    valeur = 0
    for dom in GRI:
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

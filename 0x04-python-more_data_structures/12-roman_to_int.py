#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    V = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    U = ["IX", "VIII", "VII", "VI", "V", "IV", "III", "II", "I"]
    T = ["XC", "LXXX", "LXX", "LX", "L", "XL", "XXX", "XX", "X"]
    H = ["CM", "DCCC", "DCC", "DC", "D", "CD", "CCC", "CC", "C"]
    Units = {U[i]: V[i] for i in range(9)}
    Tens = {T[i]: V[i] * 10 for i in range(9)}
    Hundreds = {H[i]: V[i] * 100 for i in range(9)}
    Thousands = {"MMM": 3000, "MM": 2000, "M": 1000}
    resume = {"Un": Units, "Te": Tens, "Hu": Hundreds, "Th": Thousands}
    rs = ""
    for e in roman_string:
        rs = f"{rs}{e}"
    valeur = 0
    for k1, v1 in resume.items():
        for k, v in v1.items():
            if k in rs:
                valeur = valeur + v
                rs = rs.replace(k, "")
                break
    if len(rs) > 0:
        return 0
    return valeur

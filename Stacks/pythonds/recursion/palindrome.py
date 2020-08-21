def reverse(in_str):
    ls = list(in_str)
    revLs = ls[::-1]
    str1 = ""
    for letter in revLs:
        str1 += str(letter)
    return str1
#print(reverse("kjuhgas"))


def removeWhite(s):
    s = s.replace(" ", "")
    return s

in_str = "huhduh gsdg"

print(removeWhite(in_str))
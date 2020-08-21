def ConvertingIntToString(num, base):
    if num < base:
        return str(num)
    else:
        return ConvertingIntToString(num//base, base) + str(num%base)

print(ConvertingIntToString(789, 10))
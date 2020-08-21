from pythonds.basic import stack as s

def getBinaryNumber(inNum):
    st1 = ""
    obj = s.stack()
    dividend = inNum
    while dividend > 0:
        reminder = dividend%2
        dividend = dividend//2
        obj.push(reminder)
    while not obj.isEmpty():
        st1 = st1 + str(obj.pop())   
    return st1

a = 24
print(getBinaryNumber(a))
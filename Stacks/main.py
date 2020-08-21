from pythonds.basic import stack as s
from pythonds.basic import Queue as q
from pythonds.basic import Deque as d

print("This is main")

"""

Obj = s.stack()

Obj.push("hello1")

print(Obj.peek())
print(Obj.pop())
print(Obj.peek())


def revstring(mystr):
    print(mystr)
    lst = list(mystr)
    #print(lst)
    newList = []
    stck = s.stack()
    for item in lst:
        stck.push(item)
    print("Size of the Stack is", stck.size())
    str = ""
    for i in range(stck.size()):
        #print(i)
        str+=stck.pop()
    return str

print("revstring is ", revstring("Hello"))


def bracesMatches(in_Str):
    print(in_Str)
    lst = list(in_Str)
    stc = s.stack()
    blnBracesMatches = False
    for item in lst:
        if item == "(":
            stc.push(item)
        elif  item == ")":
            if stc.size() != 0 :
                stc.pop()
                blnBracesMatches = True
            else:
                blnBracesMatches = False
                break            
        else:
            raise Exception("Item Invalid")
        
    if blnBracesMatches and stc.size() == 0:
        return True
    else:
        return False

print(bracesMatches("()))"))
    


q1=q.Queue()
q1.enqueue("Bill",)
q1.enqueue("David")
q1.enqueue("Susan")
q1.enqueue("Jane")
q1.enqueue("Kent")
q1.enqueue("Brad")

num = 0

while q1.size() != 1:
    num += 1
    popItem = q1.dequeue()
    #print(popItem)
    q1.enqueue(popItem)
    if num == 7:
        q1.dequeue()
        num = 0

print("Last Element left in the queue is %s and the size of the queue is %d" %(q1.LastQueueElement(),  q1.size()))


q2 = d.Deque()
q2.addFront("1")
q2.addFront("2")
q2.addRear("3")
q2.addRear("4")
q2.addRear("5")
print(q2.removeRear())
print(q2.removeFront())
print(q2.size())

"""


f = open(r"text.txt", "r")
myStack = []
myStack1 = []
myStack2 = []
myStack3 = []
myStack4 = []
myStack5 = []
myStack6 = []
myStack7 = []
myStack8 = []
myStack9 = []
natija = ''

def head(str):
    if str[0:4] != '    ':
        myStack1.append(str[0:3])
    if str[4:8] != '    ':
        myStack2.append(str[4:7])
    if str[8:12] != '    ':
        myStack3.append(str[8:11])
    if str[12:16] != '    ':
        myStack4.append(str[12:15])
    if str[16:20] != '    ':
        myStack5.append(str[16:19])
    if str[20:24] != '    ':
        myStack6.append(str[20:23])
    if str[24:28] != '    ':
        myStack7.append(str[24:27])
    if str[28:32] != '    ':
        myStack8.append(str[28:31])
    if str[32:35] != '   ':
        myStack9.append(str[32:35])

    return str


def body(str, shart):
    newlist = []
    arr = str.split(' ')
    # print(arr)
    move = int(arr[1])
    from_ = int(arr[3]) - 1
    to = int(arr[5]) - 1
    if shart == 1:
        while move > 0:
            myStack[to].append(myStack[from_].pop())
            move -= 1
    if shart == 2:
        while move > 0:
            newlist.append(myStack[from_].pop())
            move -= 1
        for ss in s(newlist):
            myStack[to].append(ss)


def s(lst):
    newlist = []
    n = len(lst)
    while True:
        newlist.append(lst.pop())
        n -= 1
        if n == 0:
            return newlist


i = 0
for x in f:
    i = i + 1
    x = x.replace('\n', '')
    if i < 9:
        head(x)
    if i == 10:
        myStack.append(s(myStack1))
        myStack.append(s(myStack2))
        myStack.append(s(myStack3))
        myStack.append(s(myStack4))
        myStack.append(s(myStack5))
        myStack.append(s(myStack6))
        myStack.append(s(myStack7))
        myStack.append(s(myStack8))
        myStack.append(s(myStack9))
    if i > 10:
        body(x, 2)

for x in myStack:
    natija = natija + x.pop()[1]
print(natija)

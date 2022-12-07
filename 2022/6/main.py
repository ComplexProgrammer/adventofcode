f = open(r"text.txt", "r")

natija = 0

import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(400000000)
print(sys.getrecursionlimit())


def aa(str):
    # print(str)
    a = 0
    for i in range(0, len(str)):
        str_ = str.replace(str[i], '')
        if len(str_) < len(str)-1:
            a = 1
            break
        # str_ = str.replace(str[i], '')
        # # print(str_)
        # if len(str_) < len(str)-1:
        #     a = 1
        #     break
        #     # print(str[i])
        #     # print(a)
    return a


def aniqla1(str, j, n):
    t = aa(str[j:j + n])
    if t == 0:
        print(str[j:j + n])
        print(j+n)
    else:
        j = j + 1
        # print(str[j + n:len(str)])
        # print(j)
        aniqla1(str, j, n)


i = 0
for x in f:
    i = i + 1
    x = x.replace('\n', '')
    print(x)
    aniqla1(x, 0, 12)

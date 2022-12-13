f = open(r"text0.txt", "r")
import numpy as np
import random
import sys
sys.setrecursionlimit(10000100)

i = 0
arr = []
arr2 = []
arr1 = []


def a(text, a1, a2):
    for t in text:
        a1.append(t)
        a2.append(ord(t))
    arr.append(a1)
    arr2.append(a2)


for x in f:
    i = i + 1
    x = x.replace('\n', '')
    a(x, [], [])

text = ''
text2 = ''
print(arr)
print(arr2)
S = [0, 0]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        a = arr[i][j]
        if ord(a) == 83:
            S[0] = i
            S[1] = j
        if a != 'Z':
            if ord(a) < 90:
                res = ord(a) - 38
            else:
                res = ord(a) - 96
        else:
            res = 52
        text = text + arr[i][j]
        # text = text + arr[i][j]+'['+res.__str__()+']'
        text2 = text2 + res.__str__()
    text = text + '\n'
    text2 = text2 + '\n'
print(text)
print(S)
left = 0


def aniqla():
    list1 = [1, 2, 3, 4]
    r = random.choice(list1)
    # print(r)
    while r:
        if r == 1:
            if S[1] > 0:
                S[1] = S[1] - 1
                arr[S[0]][S[1]] = '<'
        if r == 2:
            if S[1] < len(arr)-1:
                S[1] = S[1] + 1
                arr[S[0]][S[1]] = '>'
        if r == 3:
            if S[0] > 0:
                S[0] = S[0] - 1
                arr[S[0]][S[1]] = '^'
        if r == 4:
            if S[0] < len(arr)-1:
                S[0] = S[0] + 1
                arr[S[0]][S[1]] = 'v'
        text_ = ''
        for ii in range(len(arr)):
            for jj in range(len(arr[ii])):
                text_ = text_ + arr[ii][jj]
            text_ = text_ + '\n'
        print(text_, r, S, arr[S[0]][S[1]])
        aniqla()
        break


aniqla()
print('Tugadi  :)')

import os
import sys

import numpy as np

f = open(r"text.txt", "r")
sys.setrecursionlimit(400000000)
natija = 0
n = 1
arr1 = []
arr2 = []


def left(arr, index, el, r):
    for x in reversed(range(0, index)):
        # print(x)
        if el <= int(arr[x]):
            r = False
            break
    return r


def right(arr, index, el, r):
    for x in range(index + 1, len(arr)):
        if el <= int(arr[x]):
            r = False
            break
    return r


def left2(arr, index, el, r):
    for x in reversed(range(0, index)):
        r = r + 1
        if el <= int(arr[x]):
            break
    return r


def right2(arr, index, el, r):
    for x in range(index+1, len(arr)):
        r = r + 1
        if el <= int(arr[x]):
            break
    return r


def column(matrix, i):
    return [row[i] for row in matrix]


def a(text):
    for x in range(0, len(text)):
        arr1.append(text[x])


def aniqla(arr, n):
    for x in range(1, len(arr) - 1):
        for y in range(1, len(arr) - 1):
            if left(arr[x], y, int(arr[x][y]), True) or right(arr[x], y, int(arr[x][y]), True) or left(column(arr, y),
                                                                                                       x,
                                                                                                       int(arr[x][y]),
                                                                                                       True) or right(
                    column(arr, y), x, int(arr[x][y]), True):
                n = n + 1

    return n + 4 * (len(arr) - 1)


def aniqla2(arr, n, max):
    print(arr)
    for x in range(0, len(arr)):
        for y in range(0, len(arr)):
            n1 = left2(arr[x], y, int(arr[x][y]), 0)
            n2 = right2(arr[x], y, int(arr[x][y]), 0)
            n3 = left2(column(arr, y), x, int(arr[x][y]), 0)
            n4 = right2(column(arr, y), x, int(arr[x][y]), 0)
            n = n1*n2*n3*n4
            if max < n:
                max = n
                print(arr[x][y], n1, n2, n3, n4, max)

    return max


i = 0
j = 0
for x in f:
    i = i + 1
    x = x.replace('\n', '')
    a(x)
    arr2.append(arr1)
    arr1 = []

natija1 = aniqla(np.array(arr2), 0)
natija2 = aniqla2(np.array(arr2), 0, 0)
print(natija1)
print(natija2)
# print(natija1+natija2)

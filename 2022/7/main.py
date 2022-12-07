import os
import sys

f = open(r"text.txt", "r")
sys.setrecursionlimit(400000000)
natija = 0
n = 0

arr1 = []
arr2 = []
arr3 = []
arr4 = []
arr5 = []
arr6 = []
arr7 = []
arr8 = []
arr9 = []
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)


def tree(ar, n, i, j):
    if j == 1:
        arr1.append(i)
        arr1.append(j)
        arr1.append(ar)
    if j == 2:
        arr2.append(i)
        arr2.append(j)
        arr2.append(ar)
        # arr1.append(arr2)
    if j == 3:
        arr3.append(i)
        arr3.append(j)
        arr3.append(ar)
        # arr2.append(arr3)
    if j == 4:
        arr4.append(i)
        arr4.append(j)
        arr4.append(ar)
        # arr3.append(arr4)
    if j == 5:
        arr5.append(i)
        arr5.append(j)
        arr5.append(ar)
        # arr4.append(arr5)
    if j == 6:
        arr6.append(i)
        arr6.append(j)
        arr6.append(ar)
        # arr5.append(arr6)
    if j == 7:
        arr7.append(i)
        arr7.append(j)
        arr7.append(ar)
        # arr6.append(arr7)
    if j == 8:
        arr8.append(i)
        arr8.append(j)
        arr8.append(ar)
        # arr7.append(arr8)
    if j == 9:
        arr9.append(i)
        arr9.append(j)
        arr9.append(ar)
        # arr8.append(arr9)


def aniqla(text, n, i, j):
    if str(text).startswith('$ cd') or str(text) == '$ cd ..' or str(text) == '$ ls':
        return 0
    else:
        # print(text, '->', text.split(' ')[0])
        if text.split(' ')[0] != 'dir':
            # arr.append(text.split(' ')[0])
            tree(text.split(' ')[0], n, i, j)
            return int(text.split(' ')[0])
        else:
            # arr.append(j)
            tree(text.split(' ')[1], n, i, j)
            # if j == 2:
            #     os.mkdir(os.path.join(basedir, text.split(' ')[1]))
            return 0


n = 0
i = 0
j = 0
for x in f:
    n+1
    x = x.replace('\n', '')
    if str(x).startswith('$ cd') or str(x) == '$ cd ..' or str(x) == '$ ls':
        i = 0
        if str(x) == '$ ls':
            j = j + 1
        if str(x) == '$ cd ..':
            j = j - 1

    else:
        i = i + 1
        # print(x)
    if i == 0:
        if n < 100000:
            print(True, n, j)
            natija = natija + n
        else:
            print(False, n, j)
        n = 0
    n = n + aniqla(x, n, i, j)
    # if i > 0:
    # print(x, n, i, j)
with open('readme.txt', 'w') as f:
    f.write(arr1.__str__())
    f.write('\n')
    f.write(arr2.__str__())
    f.write('\n')
    f.write(arr3.__str__())
    f.write('\n')
    f.write(arr4.__str__())
    f.write('\n')
    f.write(arr5.__str__())
    f.write('\n')
    f.write(arr6.__str__())
    f.write('\n')
    f.write(arr7.__str__())
    f.write('\n')
    f.write(arr8.__str__())
    f.write('\n')
    f.write(arr9.__str__())
print(natija)

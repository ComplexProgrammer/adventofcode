import numpy as np

f = open(r"text0.txt", "r")
i = 0
j = 0
size = 10
s = [int(size / 2) - 1, int(size / 2) - 1]
H = [int(size / 2) - 1, int(size / 2) - 1]
T = [int(size / 2) - 1, int(size / 2) - 1]
arr1 = []
arr = []
for i in range(0, size):
    for j in range(0, size):
        arr1.append(".")
    arr.append(arr1)
    arr1 = []

# print(arr[2])
print(len(arr))
arr[s[0]][s[1]] = "s"


def aniqla():
    print(H, T)
    if (H[0] == T[0] or H[0] - T[0] == 1 or T[0] - H[0] == 1) and (H[1] == T[1] or H[1] - T[1] == 1 or T[1] - H[
        1] == 1):
        return False
    else:
        return True


def aniqla2(H):
    print(H, T)
    if (H[0] == T[0] or H[0] - T[0] == 1 or T[0] - H[0] == 1) and (H[1] == T[1] or H[1] - T[1] == 1 or T[1] - H[
        1] == 1):
        return False
    else:
        return True


ii = 0
sum = 0
str = ""
row = int(size / 2)-1
column = int(size / 2)-1
tailRow = int(size / 2)-1
tailColumn = int(size / 2)-1
count = 0
res = ""
str1 = ""
lists = []
step = 1
for x in f:
    x = x.replace('\n', '')
    a = x.split(' ')
    print(ii, x)
    # if int(a[1]) > 1:
    #     ii = ii + 1
    if a[0] == 'L':
        for i in range(0, int(a[1])):
            column = column - 1
            if tailColumn-column > step:
                tailRow = row
                tailColumn = column+step
            if arr[row][column] != "T":
                arr[row][column] = "H"
            arr[tailRow][tailColumn] = step - i
        # sum = L(H[0], H[1], int(a[1]), sum)
    if a[0] == 'R':
        for i in range(0, int(a[1])):
            column = column + 1
            if column-tailColumn > step:
                tailRow = row
                tailColumn = column-step
                arr[tailRow][tailColumn] = i
            if arr[row][column] != "T":
                arr[row][column] = "H"
        # sum = R(H[0], H[1], int(a[1]), sum)
    if a[0] == 'U':
        for i in range(0, int(a[1])):
            row = row - 1
            if tailRow-row > step:
                tailRow = row + step
                tailColumn = column
                arr[tailRow][tailColumn] = int(a[1]) - i
            if arr[row][column] != "T":
                arr[row][column] = "H"
        # sum = U(H[0], H[1], int(a[1]), sum)
    if a[0] == 'D':
        for i in range(0, int(a[1])):
            row = row + 1
            if row - tailRow > step:
                tailRow = row-step
                tailColumn = column
                arr[tailRow][tailColumn] = int(a[1]) - i
            if arr[row][column] != "T":
                arr[row][column] = "H"
            # arr[tailRow][tailColumn] = "T"
        # sum = D(H[0], H[1], int(a[1]), sum)
    res = ""
# print(R(s[0], s[1], 4))
# print(np.array(arr))
# print(U(s[0], s[1], 4))
mat = np.matrix(arr)
# mat = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
file = open("file.txt", "w+")
content = arr.__str__()
file.write(content)
file.close()
natija = 0
# print(np.array(arr))
text = ''
for i in range(0, size):
    for j in range(0, size):
        # if arr[i][j] == 'H':
        #     arr[i][j] = '.'
        # if arr[i][j] == 'T':
        #     arr[i][j] = '#'
        #     natija = natija + 1
        text = text + arr[i][j].__str__()
    print(text)
    text = ''

# print(arr)
# print(sum)
# print(natija)
# print(np.array(arr))

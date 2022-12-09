import numpy as np

f = open(r"text.txt", "r")
i = 0
j = 0
size = 700
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

print(s)
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


def L(i, j, n, sum):
    first = True
    H[0] = i
    H[1] = j - n
    if aniqla():
        if arr[i][j - n] != 'T':
            arr[i][j - n] = "H"
        for x in reversed(range(1, n)):
            if aniqla2([i, j - x]):
                sum = sum + 1
                arr[i][j - x] = "T"
            else:
                if first:
                    if aniqla():
                        sum = sum + 1
                    arr[i][j - x] = "T"
                    first = False
                if arr[i][j - x] != "T":
                    arr[i][j - x] = "H"
            # arr[i][j - n + x] = "T"
        T[0] = i
        T[1] = j - n + 1
    return sum


def R(i, j, n, sum):
    first = True
    H[0] = i
    H[1] = j + n
    if aniqla():
        if arr[i][j + n] != 'T':
            arr[i][j + n] = "H"
        for x in reversed(range(1, n)):
            # arr[i][j + x] = "T"
            if aniqla2([i, j + x]):
                sum = sum + 1
                arr[i][j + x] = "T"

            else:
                if first:
                    if aniqla():
                        sum = sum + 1
                    arr[i][j + x] = "T"
                    first = False
                if arr[i][j + x] != 'T':
                    arr[i][j + x] = "H"
            # arr[i][j + n - x] = "T"
        T[0] = i
        T[1] = j + n - 1
    return sum


def U(i, j, n, sum):
    first = True
    H[0] = i - n
    H[1] = j
    if aniqla():
        if arr[i - n][j] != 'T':
            arr[i - n][j] = "H"
        for x in reversed(range(1, n)):
            if aniqla2([i - x, j]):
                sum = sum + 1
                arr[i - x][j] = "T"
            else:
                if first:
                    if aniqla():
                        sum = sum + 1
                    arr[i - x][j] = "T"
                    first = False
                if arr[i - x][j] != 'T':
                    arr[i - x][j] = "H"
            # arr[i - n + x][j] = "T"
        T[0] = i - n + 1
        T[1] = j
    return sum


def D(i, j, n, sum):
    first = True
    H[0] = i + n
    H[1] = j
    if aniqla():
        if arr[i + n][j] != 'T':
            arr[i + n][j] = "H"
        for x in reversed(range(1, n)):
            if aniqla2([i + x, j]):
                sum = sum + 1
                arr[i + x][j] = "T"
            else:
                if first:
                    if aniqla():
                        sum = sum + 1
                    arr[i + x][j] = "T"
                    first = False
                if arr[i + x][j] != 'T':
                    arr[i + x][j] = "H"
            # arr[i + n - x][j] = "T"
        T[0] = i + n - 1
        T[1] = j
    return sum


ii = 0
sum = 0
for x in f:
    x = x.replace('\n', '')
    a = x.split(' ')
    print(ii, x)
    # if int(a[1]) > 1:
    #     ii = ii + 1
    if a[0] == 'L':
        sum = L(H[0], H[1], int(a[1]), sum)
    if a[0] == 'R':
        sum = R(H[0], H[1], int(a[1]), sum)
    if a[0] == 'U':
        sum = U(H[0], H[1], int(a[1]), sum)
    if a[0] == 'D':
        sum = D(H[0], H[1], int(a[1]), sum)

# print(R(s[0], s[1], 4))
print(np.array(arr))
# print(U(s[0], s[1], 4))
mat = np.matrix(arr)
# mat = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
file = open("file.txt", "w+")
content = str(arr)
file.write(content)
file.close()
natija = 0
for i in range(0, size):
    for j in range(0, size):
        if arr[i][j] == 'H':
            arr[i][j] = '.'
        if arr[i][j] == 'T':
            arr[i][j] = '#'
            natija = natija + 1
print(natija)
print(sum)
print(np.array(arr))

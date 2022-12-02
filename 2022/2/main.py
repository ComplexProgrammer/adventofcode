f = open(r"C:\Users\User\PycharmProjects\adventofcode\2022\2\text.txt", "r")
sum = 0
result = 0
# for x in f:
#     if x == 'A X' or x == 'A X\n':
#         sum = sum + 4
#     if x == 'A Y' or x == 'A Y\n':
#         sum = sum + 8
#     if x == 'A Z' or x == 'A Z\n':
#         sum = sum + 3
#     if x == 'B X' or x == 'B X\n':
#         sum = sum + 1
#     if x == 'B Y' or x == 'B Y\n':
#         sum = sum + 5
#     if x == 'B Z' or x == 'B Z\n':
#         sum = sum + 9
#     if x == 'C X' or x == 'C X\n':
#         sum = sum + 7
#     if x == 'C Y' or x == 'C Y\n':
#         sum = sum + 2
#     if x == 'C Z' or x == 'C Z\n':
#         sum = sum + 6

for x in f:
    arr = x.split(' ')
    if arr[1] == 'X' or arr[1] == 'X\n':
        if arr[0] == 'A':
            sum = sum + 3
        if arr[0] == 'B':
            sum = sum + 1
        if arr[0] == 'C':
            sum = sum + 2
    if arr[1] == 'Y' or arr[1] == 'Y\n':
        if arr[0] == 'A':
            sum = sum + 4
        if arr[0] == 'B':
            sum = sum + 5
        if arr[0] == 'C':
            sum = sum + 6

    if arr[1] == 'Z' or arr[1] == 'Z\n':
        if arr[0] == 'A':
            sum = sum + 8
        if arr[0] == 'B':
            sum = sum + 9
        if arr[0] == 'C':
            sum = sum + 7


print(sum)


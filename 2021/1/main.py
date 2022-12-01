f = open(r"C:\Users\User\PycharmProjects\adventofcode\2021\1\text.txt", "r")
max = 0
sum = 0
for x in f:
    if max < int(x):
        max = int(x)
        sum = sum + 1
    else:
        max = 0
        sum = 0


print(sum)

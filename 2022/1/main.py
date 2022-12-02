f = open(r"C:\Users\User\PycharmProjects\adventofcode\2022\1\text3.txt", "r")
max = 0
sum = 0
for x in f:
    if x != '\n':
        sum = sum+int(x)
    else:
        if max<sum:
            max = sum
        sum = 0
print(max)
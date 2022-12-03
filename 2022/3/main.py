f = open(r"C:\Users\User\PycharmProjects\adventofcode\2022\3\text.txt", "r")
sum = 0
result = 0
for x in f:
    print(x)
    print(x[0:int((len(x)+1)/2)])
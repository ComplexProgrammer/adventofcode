f = open(r"text0.txt", "r")
sum = 0
n = 20
result = 1
natija1 = 0
i = 0
for x in f:
    i = i + 1
    x = x.replace('\n', '')
    cycle = x.split()[0]
    if cycle == 'noop':
        v = 0
        sum = sum + 1
    if cycle == 'addx':
        v = int(x.split()[1])
        sum = sum + 2

    if sum >= n:
        natija1 = natija1 + n * result
        print('<~~~~~~~~~~~~>', natija1, n, result)
        n = n + 40
    result = result + v
print(natija1)
text = '#'
for i in range(40):
    text = text + '.'
text = text + '#'
for i in range(6):
    print(text)

f = open(r"text0.txt", "r")
import numpy as np

sum = 0
result = 1
natija1 = 0
i = 0
Monkey = []
Starting = []
Operation = []
Test = []
true = []
false = []
arr = []
arr2 = []
arr1 = []
for x in f:
    i = i + 1
    x = x.replace('\n', '')
    # print(x)
    if x.startswith('Monkey '):
        x = x.replace('Monkey ', '').replace(':', '')
        Monkey.append(x)
    if x.startswith('  Starting items: '):
        x = x.replace('  Starting items: ', '')
        for j in x.split(', '):
            arr1.append(j)
        Starting.append(arr1)
        arr.append(0)
        arr2.append(np.array(arr1).size)
        arr1 = []
    if x.startswith('  Operation: '):
        x = x.replace('  Operation: ', '')
        Operation.append(x)
    if x.startswith('  Test: divisible by '):
        x = x.replace('  Test: divisible by ', '')
        Test.append(x)
    if x.startswith('    If true: throw to monkey '):
        x = x.replace('    If true: throw to monkey ', '')
        true.append(x)
    if x.startswith('    If false: throw to monkey '):
        x = x.replace('    If false: throw to monkey ', '')
        false.append(x)

# print('arr', arr)
# print('Monkey', Monkey)
# print('Starting', Starting)
# print('Operation', Operation)
# print('Test', Test)
print('true', true)
print('false', false)
print('Starting', Starting)
new = ''
r = []
result = 0
for i in range(20):
    for m in Monkey:
        for o in Starting[int(m)]:
            new = Operation[int(m)].replace('new = ', '').replace('old', o)
            r = new.split()
            # arr[int(m)] = arr[int(m)] + 1
            if r[1] == '*':
                result = int(r[0]) * int(r[2])
            if r[1] == '/':
                result = int(r[0]) / int(r[2])
            if r[1] == '-':
                result = int(r[0]) - int(r[2])
            if r[1] == '+':
                result = int(r[0]) + int(r[2])
            rr = int(result / 3)
            # rr = int(result)
            # print(m, new + ' = ' + result.__str__(), int(result / 3), rr, Test[int(m)], true[int(m)], false[int(m)])
            # print('Starting', Starting, arr2, rr, Test[int(m)], result, int(result)/int(Test[int(m)]))
            # if rr / int(Test[int(m)]) - int(rr / int(Test[int(m)])) == 0:
            if rr / int(Test[int(m)]) - int(rr / int(Test[int(m)])) == 0:
            # if int(result) / int(Test[int(m)]) - int(int(result) / int(Test[int(m)])) == 0:
            # if not round(int(rr) / int(Test[int(m)])):
                # print(result / int(Test[int(m)]) - int(result / int(Test[int(m)])))
                Starting[int(true[int(m)])].append(rr.__str__())
                # Starting[int(true[int(m)])].append(round(int(rr)/int(Test[int(m)])).__str__())
                # print(m, new + ' = ' + result.__str__(), rr, Test[int(m)], true[int(m)], True)
            else:
                Starting[int(false[int(m)])].append(rr.__str__())
                # Starting[int(false[int(m)])].append(result.__str__())
                # Starting[int(false[int(m)])].append(round(int(rr) / int(Test[int(m)])).__str__())
                # print(m, new + ' = ' + result.__str__(), rr, Test[int(m)], false[int(m)], False)
            arr2[int(m)] = np.array(Starting[int(m)]).size
        # print(m, arr[int(m)], arr2[int(m)], Starting[int(m)])
        if np.array(Starting[int(m)]).size >= int(arr2[int(m)]):
            arr[int(m)] = arr[int(m)] + arr2[int(m)]
        else:
            arr[int(m)] = arr[int(m)] + np.array(Starting[int(m)]).size
        Starting[int(m)] = Starting[int(m)][int(arr2[int(m)]):]
        # print(m, arr[int(m)], arr2[int(m)], Starting[int(m)])
    print('Starting', Starting, i + 1)
    # for s in range(len(Starting)):
    #     print(s, arr[s], arr2[s], Starting[s])
    #     if np.array(Starting[s]).size >= int(arr2[s]):
    #         arr[int(s)] = arr[int(s)] + arr2[s]
    #     else:
    #         arr[int(s)] = arr[int(s)] + np.array(Starting[s]).size
    #         print(np.array(Starting[s]).size)
    #     Starting[s] = Starting[s][int(arr2[s]):]
    #     print(s, arr[s], arr2[s], Starting[s])
    # print('Starting', Starting, i+1)
print('arr', arr)
print('arr2', arr2)

# for i in range(len(arr)):
#     arr[i] = arr[i] - arr2[i]
max1 = 0
for i in arr:
    if i > max1:
        max1 = i
arr.remove(max1)
max2 = 0
for i in arr:
    if i > max2:
        max2 = i
print(max1.__str__() + ' * ' + max2.__str__() + " = " + (max1 * max2).__str__())

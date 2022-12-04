f = open(r"text.txt", "r")

natija1 = 0
natija2 = 0


def aniqla1(str):
    arr1 = str.split(',')[0].split('-')
    arr2 = str.split(',')[1].split('-')
    if (int(arr1[0]) >= int(arr2[0]) and int(arr1[1]) <= int(arr2[1])) or (int(arr1[0]) <= int(arr2[0]) and int(arr1[1]) >= int(arr2[1])):
        return 1
    else:
        return 0


def aniqla2(str):
    arr1 = str.split(',')[0].split('-')
    arr2 = str.split(',')[1].split('-')
    if (int(arr1[1]) >= int(arr2[0]) and int(arr1[0]) <= int(arr2[1])) or (int(arr2[1]) >= int(arr1[0]) and int(arr2[0]) <= int(arr1[1])):
        return 1
    else:
        return 0


for x in f:
    x = x.replace('\n', '')
    natija1 = natija1 + aniqla1(x)
    natija2 = natija2 + aniqla2(x)
print(natija1)
print(natija2)

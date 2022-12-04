f = open(r"text.txt", "r")

natija1 = 0
natija2 = 0


def aniqla1(str1, str2):
    for a in str1:
        for b in str2:
            if a == b:
                if a != 'Z':
                    if ord(a) < 90:
                        res = ord(a) - 38
                    else:
                        res = ord(a) - 96
                else:
                    res = 52
                print(a + " : " + str(res))
                return res


def aniqla2(str1, str2, str3):
    for a in str1:
        for b in str2:
            for c in str3:
                if a == b == c:
                    if a != 'Z':
                        if ord(a) < 90:
                            res = ord(a) - 38
                        else:
                            res = ord(a) - 96
                    else:
                        res = 52
                    print(a + " : " + str(res))
                    return res


i = 0
for x in f:
    i = i+1
    x = x.replace('\n', '')
    natija1 = natija1 + aniqla1(x[0:int(len(x) / 2)], x[int(len(x) / 2):len(x)])
    if i == 1:
        x1 = x
    if i == 2:
        x2 = x
    if i == 3:
        i = 0
        natija2 = natija2 + aniqla2(x1, x2, x)
print(natija1)
print(natija2)

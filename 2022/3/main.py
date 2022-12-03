f = open(r"C:\Users\User\PycharmProjects\adventofcode\2022\3\text2.txt", "r")

natija = 0


# def aniqla(str1, str2):
#     for a in str1:
#         for b in str2:
#             if a == b:
#                 if a != 'Z':
#                     if ord(a) < 90:
#                         res = ord(a) - 38
#                     else:
#                         res = ord(a) - 96
#                 else:
#                     res = 52
#                 print(a + " : " + str(res))
#                 return res
#
#
# for x in f:
#     x = x.replace('\n', '')
#     natija = natija + aniqla(x[0:int(len(x) / 2)], x[int(len(x) / 2):len(x)])
def aniqla(str1, str2, str3):
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
    if i == 1:
        x1 = x
    if i == 2:
        x2 = x
    if i == 3:
        i = 0
        natija = natija + aniqla(x1, x2, x)
print(natija)

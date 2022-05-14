_input = input()
kol = 0
for i in range(int(_input)):
    _input2 = input()
    x=_input2.split()
    kol=0
    for j in range(int(x[0])):
        kol += int(x[j + 1])
    print(kol - int((x[0])) + 1)

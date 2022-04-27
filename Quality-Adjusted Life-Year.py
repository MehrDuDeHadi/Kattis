_input1 = input()
SUM = 0
for i in range(int(_input1)):
    _input2 = input()
    a, b = _input2.split()
    SUM += float(a) * float(b)
print(SUM)
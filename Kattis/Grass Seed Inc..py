cost = input()
_input = input()
SUM = 0
for i in range(int(_input)):
    _input2 = input()
    a, b = _input2.split()
    SUM += float(a) * float(b)
print(float(cost) * SUM)

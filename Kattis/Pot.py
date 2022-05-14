_input1 = input()
SUM = 0
kh = 0
baq = 0
for i in range(int(_input1)):
    _input2 = input()
    baq = int(_input2) % 10
    kh = int(_input2) / 10
    SUM += pow(int(kh), baq)
print(SUM)

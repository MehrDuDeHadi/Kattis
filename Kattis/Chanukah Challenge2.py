_input = input()
jam = 0
k = 1
for i in range(int(_input)):
    _input2 = input()
    line = _input2.split('\n')
    for j in line:
        a, b = j.split()
        for k in range(int(b) + 1):
            jam += k
        print(a, (jam) + int(b))
        jam = 0
        k = 0

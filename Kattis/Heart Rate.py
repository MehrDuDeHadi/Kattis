_input = input()
output = ''
for i in range(int(_input)):
    _input2 = input()
    a, b = _input2.split()
    bpm = int(a) * 60 / float(b)
    MIN = (int(a) * 60 / float(b)) - (60 / float(b))
    MAX = (60 / float(b)) + (int(a) * 60 / float(b))
    output += str(MIN) + ' ' + str(bpm) + ' ' + str(MAX) + '\n'
print(output)

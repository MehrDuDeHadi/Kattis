_input = input()
output =''
for i in range(int(_input)):
    _input2 = input()
    a, b, c = _input2.split()
    if int(a) + int(c) < int(b):
        output = output + 'advertise' + '\n'
    elif int(a) + int(c) > int(b):
        output = output + 'do not advertise' + '\n'
    elif int(a) + int(c) == int(b):
        output = output + 'does not matter' + '\n'
print(output)
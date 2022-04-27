_input1 = input()
_input2 = input()
if int(_input2) > 0 and int(_input1) > 0:
    print('1')
elif int(_input2) < 0 and int(_input1) < 0:
    print('3')
elif int(_input2) < 0 and int(_input1) > 0:
    print('4')
elif int(_input2) > 0 and int(_input1) < 0:
    print('2')

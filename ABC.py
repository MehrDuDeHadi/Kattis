_input1 = input()
_input2 = input()
a, b, c = _input1.split()
if (a > c):
    a, c = c, a
if (b > c):
    b, c = c, b
if (a > b):
    a, b = b, a
if _input2 == 'ABC':
    print(a, b, c)
if _input2 == 'ACB':
    print(a, c, b)
if _input2 == 'BAC':
    print(b, a, c)
if _input2 == 'BCA':
    print(b, c, a)
if _input2 == 'CAB':
    print(c, a, b)
if _input2 == 'CBA':
    print(c, b, a)

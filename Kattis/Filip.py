_input = input()
z = 1
b1 = b2 = 0
a1, a2 = _input.split()
for i in a1:
    b1 += int(i) * z
    z = z * 10
z = 1
for i in a2:
    b2 += int(i) * z
    z = z * 10
if b1 > b2:
    print(b1)
else:
    print(b2)

_input = input()
_input2 = input()
c = 0
x = _input2.split()
for i in x:
    if int(i) < 0:
        c += 1
print(c)

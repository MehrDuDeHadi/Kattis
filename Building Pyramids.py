_input = input()
a = 1
j = 0
SUM = 0
while SUM <= int(_input):
    SUM += a * a
    a += 2
    j += 1
print(j-1)

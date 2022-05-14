_input = input()
l1 = []
total = 0
gcv, trc, n = _input.split()
_input2 = input()
l1 = _input2.split()
for i in l1:
    total += int(i)
print(int(((int(gcv) - int(trc)) * 0.9) - total))

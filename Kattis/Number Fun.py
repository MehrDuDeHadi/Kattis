line = input()
a=[]
for i in range(int(line)):
    a.append([int(j) for j in input().split()])
for row in range(len(a)):
    if (a[row][0] + a[row][1] == a[row][2]) or \
        (a[row][0] - a[row][1] == a[row][2]) or\
        (a[row][0] * a[row][1] == a[row][2]) or \
        (a[row][0] / a[row][1] == a[row][2]) or \
        (a[row][1] - a[row][0] == a[row][2]) or\
        (a[row][1] / a[row][0] == a[row][2]):
        print('possible')
    else :
        print('impossible')
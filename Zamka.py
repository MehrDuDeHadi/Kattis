def zamka(v1, v2, v3):
    for i in range(int(v1), int(v2)):
        count = 0
        for j in str(i):
            count += int(j)
        if int(v3) == count:
            print(i)
            break
    for i in range(int(v2), int(v1), -1):
        count = 0
        for j in str(i):
            count += int(j)
        if int(v3) == count:
            print(i)
            break
a1 = input()
a2 = input()
a3 = input()
zamka(a1, a2, a3)

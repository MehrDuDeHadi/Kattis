tedad =input()
a=[]
kol=0
if  int(tedad) % 2 == 1 :
    print('still running')
else :
    for i in range(int(tedad)) :
        a.append(input())
    for j in range(len(a)) :
        if  j % 2 == 0 :
            kol+=int(a[j+1]) - int(a[j])
    print(kol)

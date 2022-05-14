n=input()
i=0
j=0
a=['']
while i < int(n) :
    a.append(input())
    i+=1
for j in range(i+1) :
    if j % 2 ==1 :
        print(a[j])
    j=+1

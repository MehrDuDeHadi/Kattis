_input = input()
__input = input()
doc=jun=0
for line in _input :
    if line =='a' :
        jun +=1
for line in __input :
    if line =='a' :
        doc +=1
if jun >= doc :
    print('go')
else :
    print('no')

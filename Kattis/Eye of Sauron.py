_input=input()
x=_input.find('(')
if _input[:x] == _input[x+2:] :
    print('correct')
else :
    print('fix')

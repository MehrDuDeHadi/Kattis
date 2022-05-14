answer = str()
for i in range(int(input())):
    in__ = input()
    if 'Simon says ' in in__:
        in__ = in__.replace('Simon says ', '')
        answer += in__ + '\n'

print(answer)

result = str()
for i in range(int(input())):
    _input = input()
    if _input[:len('Simon says ')] == 'Simon says ':
        print(_input[len('Simon says '):])

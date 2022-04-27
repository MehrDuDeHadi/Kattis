operators=['=','*','+']
numbers=['1']
count =0
fact = open('az.txt').read()
program = fact.split('\n')
for line in program :
    count = count +1
    print('line', count, '\n', line)
    tokens = line.split(' ')
    print('tokens are', tokens)
    for token in tokens :
        if token in operators :
            print(token, ' is operator')
        elif token in numbers :
            print(token, ' is number')
    print('-------------------------')
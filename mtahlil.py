count=0
fact = open('az.txt').read()
program = fact.split('\n')
for line in program :
    count = count +1
    print('line', count, '\n', line)
    tokens = line.split(' ')
    print('tokens are', tokens)
    for token in tokens :
        if token.isidentifier() :
            print(token, ' is identifier')
        elif token.isdigit() :
            print(token, 'is digit')
    print('-------------------------')

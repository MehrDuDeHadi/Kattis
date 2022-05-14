_input = input()
for i in range(len(_input) - 1):
    if _input[i] == ';' or _input[i] == ':':
        if _input[i + 1] and _input[i + 1] == ')':
            print(i)
        if _input[i + 1] == '-' and _input[i + 2] == ')':
            print(i)

def lastdigit(num):
    last = str(num[0] - num[1])
    if last[-1] == '0':
        return 'true'
    else:
        return "false"


print(lastdigit([int(input()) for i in range(2)]))

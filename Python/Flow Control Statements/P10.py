def palindrome(num):
    i = 1
    while (i <= len(num)):
        if num[i-1] != num[-i]:
            return f'{num} is not a palindrome'
        i += 1
    else:
        return f'{num} is a palindrome'


print(palindrome(input()))

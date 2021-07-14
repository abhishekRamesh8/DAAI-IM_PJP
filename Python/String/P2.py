str = input()
for i in range(1, len(str) + 1):
    if str[i-1] != str[-i]:
        print("Given string is not a palindrome")
        break
else:
    print(f"{str} is a Palindrome")
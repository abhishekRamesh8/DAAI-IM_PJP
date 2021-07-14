str = input()

if len(str) >= 2:
    print(str[:2] * len(str))
else:
    print("The input string should be greater than 2")

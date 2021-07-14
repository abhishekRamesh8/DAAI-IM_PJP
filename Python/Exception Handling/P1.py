num1 = int(input())
num2 = int(input())

try:
    print(num1 // num2)
except Exception as e:
    print(e)
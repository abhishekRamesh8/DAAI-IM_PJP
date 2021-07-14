myList = list(range(1, 21, 2))

index = int(input())

try:
    if myList[index] > 0:
        print("Positive number")
    else:
        print(myList[index])
        print("Negative number")
except Exception as e:
    print(e)
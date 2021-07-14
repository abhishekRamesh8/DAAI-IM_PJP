import sys

myList = list(map(int, sys.argv[1:]))
count = 0
for i in myList:
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        count += i

print(count)

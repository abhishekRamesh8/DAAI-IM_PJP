list1 = []
MyTup = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
for i in MyTup:
    i = i[:-1] + (100,)
    list1.append(i)
print(list1)


MyList1 = list(range(0, 5))
MyList2 = [11, 21]
j = 0
for i in MyList2:
    MyList1.insert(j, i)
    j += 1

print(MyList1)
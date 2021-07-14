Mydic1 = dict()
total = 0
for i in range(0, 5):
    Mydic1[i] = i * 2
    total += Mydic1[i]
print("values: ", [i for i in Mydic1.values()])
print(total)

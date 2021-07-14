Mydic1 = dict()
for i in range(0, 5):
    Mydic1[i] = i * 10

Mydic2 = {5: 50}
Mydic1.update(Mydic2)

print(Mydic1)
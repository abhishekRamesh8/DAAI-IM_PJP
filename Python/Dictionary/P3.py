Mydic1 = dict()
for i in range(0, 5):
    keys = input()
    if keys in Mydic1.keys():
        print(f'The key {i} already exists')
        continue
    Mydic1[keys] = i * 10
print(Mydic1)



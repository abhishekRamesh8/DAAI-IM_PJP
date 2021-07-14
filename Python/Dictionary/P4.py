Mydic1 = dict()
for i in range(0, 5):
    Mydic1[i] = i * 2
keys = []
values = []
for key, value in Mydic1.items():
    keys.append(key)
    values.append(value)
print("Key: ", keys)
print("value : ", values)
print(f"Keys={keys}, values={values}")

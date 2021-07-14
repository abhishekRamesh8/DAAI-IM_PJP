myList = []
with open("demo.txt", 'r') as f:
    line = f.readline()
    while line:
        myList.append(line.strip())
        line = f.readline()

print(myList)
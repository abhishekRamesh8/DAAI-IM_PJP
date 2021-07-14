with open("demo.txt", 'r') as f:
    max = ' '
    words = f.read().split()
    for i in words:
        if len(i) > len(max):
            max = i

print(max)

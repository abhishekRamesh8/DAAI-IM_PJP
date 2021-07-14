
file = input()
try:
    with open(file, 'r') as f:
        print(f.read().upper())
except Exception as e:
    print(e)

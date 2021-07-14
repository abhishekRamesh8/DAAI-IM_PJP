with open("demo.txt", 'r') as f:
    word = input()
    occur = 0
    words = f.read().split()
    for i in words:
        if i == word:
            occur += 1

print(f"'{word}' occurs {occur} times")

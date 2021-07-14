file = open('demo.txt', 'r')

num = int(input("Enter the number of lines to be read: "))
for i in file.readlines()[:num]:
    print(i)


file.close()

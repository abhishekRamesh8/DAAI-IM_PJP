file = open('demo.txt', 'r+')
file.writelines("""Reading list from the file, the file that was written in the example above is read in this example. 
The file is opened using the open() method in read r mode. The data read from the file is printed to the output screen. 
The file opened is closed using the close() method.""")
file.seek(0)
print(file.read())
file.close()

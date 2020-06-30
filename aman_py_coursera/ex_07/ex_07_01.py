file = input('Enter a file name: ')
handle = open(file)
read= handle.read()
print(read.upper())
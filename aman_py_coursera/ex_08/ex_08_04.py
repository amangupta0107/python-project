file = input('Enter file: ')
handle = open(file)
read = handle.read()
#print(read)
s = read.split()
#print(s)
array = list(s)
#print(array)
array.sort()
print(array)
x=[]
for final in array:
    if final not in x:
        x.append(final)
        continue
print(x)
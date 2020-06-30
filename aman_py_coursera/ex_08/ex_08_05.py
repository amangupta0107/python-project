file = input('Enter a file name: ')
handle = open(file)
#read = handle.read()
count=0
for line in handle:
    if line.startswith("From "):
        l=line.rstrip()
        
        x=l.split()
        print(x[1])
        count = count + 1
print('There were', count, 'lines in the file with From as the first word')
file = input('Enter the name of the file')
handle = open(file)
d={}
array=[]

for line in handle:
    if line.startswith('From '):
        l=line.rstrip()
        sp=l.split()
        #print(sp[2])
        #print[sp[2]]
        array.append(sp[2])
for i in array:
    d[i]=d.get(i,0)+1        
print(d)
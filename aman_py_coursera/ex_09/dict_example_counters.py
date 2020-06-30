word='brontosaurus'
d={}
#for i in word:
#	if i not in d:
#		d[i]= 1
#	else:
#		d[i]= d[i]+1
for i in word:
    d[i]=d.get(i,0) +1
print(d)
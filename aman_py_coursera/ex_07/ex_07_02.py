file = input('Enter a file name: ')
handle = open(file)
#read= handle.read()
total = 0.0
count = 0
for line in handle:
   if line.startswith('X-DSPAM-Confidence:'):
    
    l = line.rstrip()
    colon = l.find(':')
    #print (l)
    number = float(l[colon+2:])
    total = total + number
    count = count + 1
    
print(total)
print(count)
print('Average spam confidence:', total/count)
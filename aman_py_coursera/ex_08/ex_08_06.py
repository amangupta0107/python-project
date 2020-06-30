x=[]

while True:
	number = input('Enter a number: ')
	if number == 'done':
		break
	else:
		num = float(number)
	
	x.append(num)
print('Maximum',max(x))
print('Minimum',min(x))
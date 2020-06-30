
count = 0
total = 0
x = list()
while True:
    try:
        
            number = input('Enter a number: ')
            if number == 'done':
                break
            num = float(number)
            x.append(num)
            #count= count + 1
            #total = total + num
                   
    except:
        print('Invalid input')
        
print('Maximum:',max(x),'Minimum:',min(x))
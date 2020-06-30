
count = 0
total = 0
while True:
    try:
        
            number = input('Enter a number: ')
            if number == 'done':
                break
            num = float(number)
            count= count + 1
            total = total + num
                   
    except:
        print('Invalid input')
        
print(count, total, total/count)

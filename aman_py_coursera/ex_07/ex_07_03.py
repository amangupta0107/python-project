try:
   file = input('Enter the file name: ')
   if file == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    #break
   else:
    hand = open(file)
   
except:
    print('File Cannot be opened:', file)  
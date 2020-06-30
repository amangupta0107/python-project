
try:
    hours = input('Enter Hours: ')
    hr = float(hours)
    rate = input('Enter Rate: ')
    r = float(rate)
    if hr > 40:
        ot = 0
        hrot = hr - 40
        ot = hrot * (r * 1.5)
    pay = 40 * r + ot
    print('Pay:', pay)
except:
    print('Error, please enter numeric input')


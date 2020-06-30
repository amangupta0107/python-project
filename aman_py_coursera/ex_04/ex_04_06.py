

def computepay(hours,rate):
    hr = float(hours)
    r = float(rate)
    ot = 0
    if hr > 40:
        
        hrot = hr - 40
        ot = hrot * (r * 1.5)
        pay = 40 * r + ot
    else:
        pay = hr * r
    return pay

hours = input('Enter Hours: ')
rate = input('Enter Rate: ')


print('Pay:', computepay(hours,rate))

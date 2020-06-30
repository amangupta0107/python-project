while True:
    score = input('Enter score: ')

    try:
        sc = float(score)
        if sc> 1.0: print('Bad score')
        elif sc >= 0.9: print('A')
        elif sc >= 0.8: print('B')
        elif sc>= 0.7: print('C')
        elif sc>= 0.6: print('D')
        elif sc < 0.6: 
            print('F')
            break
       
    except:
        print('Bad score')

    
  
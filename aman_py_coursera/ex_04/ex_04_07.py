
def computegrade(score):
    
    try:
        sc = float(score)
        if sc> 1.0: return 'Bad score'
        elif sc >= 0.9: return 'A'
        elif sc >= 0.8: return 'B'
        elif sc>= 0.7: return 'C'
        elif sc>= 0.6: return 'D'
        elif sc < 0.6: 
            return 'F'
            
            
       
    except:
        return 'Bad score'
        
while True:
    score = input('Enter score: ')
    print(computegrade(score))
    result = computegrade(score)
    if result == 'F':
        break
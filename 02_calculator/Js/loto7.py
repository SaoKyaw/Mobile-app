import itertools


    
def posiblaty(a, b):
    
    num = []
    pair = []
    
    for i in range(1, a + 1):
        if i not in num:
            num.append(str(i))
            
     
    for i in range(b, b + 1):
#        print(sum(1 for pair in itertools.combinations_with_replacement(num, i)))
        print(len([pair for pair in itertools.combinations_with_replacement(num, i)]))
        
    return pair


    
    
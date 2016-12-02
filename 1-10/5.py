def isDivisible(N, m):

    for i in range(1, m+1):   
        
        if N % i != 0:
            
            return False
            
    return True
    

def smallestMultiple(m):

    N = 2520   
    
    x = 1
    
    while not isDivisible(N, m):
        
        N = 2520
        
        x += 1
        
        N *= x
        
    return N
    
print smallestMultiple(25)
    

def A(n, m):

    return n**2 - m**2
    
def B(n, m):
    
    return 2*n*m
    
def C(n, m):
    
    return n**2 + m**2
    


def find_triple(s):

    a, b, c = 0, 0, 0

    n = 2

    m = 1
    
    while n**2 + m**2 < s:
        
        for i in range(1, n):
                    
            a = A(n, i)
        
            b = B(n, i)
        
            c = C(n, i)

            if a + b + c == s:
            
                return (a, b, c)
       
        n += 1
        
    return 'No triple exists.'
    
print find_triple(1000)
import math

def listDivisors(n):

    divisors = []

    for i in range(1, int(math.sqrt(n))+1):
        
        if n % i == 0 and i not in divisors:
            
            divisors.append(i)
            
            divisors.append(n/i)
            
    return divisors
    
def nthTriangleNum(N):
    
    triangle_num = 0
    
    for i in range(N+1):
        
        triangle_num += i
        
    return triangle_num


divisors = []

N = 1

i = 1

limit = 500

while len(divisors) <= limit:
    
    N += i
    
    divisors = listDivisors(N-1)
    
    i += 1
    
print max(divisors)
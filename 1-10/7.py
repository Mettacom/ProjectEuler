import math

def isPrime(n, primes):
    
    root = math.sqrt(n)
    
    for i in primes:
        
        if n % i == 0:
            
            return False
            
    for j in range(primes[-1], int(root)):
        
        if n % j == 0:
            
            return False
            
    return True
        
        
    
    
    
    
def primeFinder(x):
    
    primes = [2, 3, 5, 7]
    
    n = primes[-1]
    
    while len(primes) < x:
        
        if isPrime(n, primes):
            
            primes.append(n)
            
        n += 1
            
    return primes[x-1]
    
    
            
    
    
print primeFinder(10001)

#def primes_below(n):
#    
#    
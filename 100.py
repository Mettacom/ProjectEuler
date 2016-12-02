import math

def f(y):
    
    x = math.floor(y*math.sqrt(0.5))
    
    test = (x**2 - x)/(y**2-y)
    
    if test < 0.5:
        
        while test < 0.5:
        
            x += 1
        
            test = (x**2 - x)/(y**2 - y)
            
    else:
        
        while test >= 0.5:
            
            x -= 1
            
            test = (x**2 - x)/(y**2 - y)
        
    return (int(x), test)
    
initial = 10

x = 0

while x != 0.5:
    
    x = f(initial)[1]
    
    initial += 1
    
print f(initial -1)



#def g(x, y):
#    
#    return (float(x)**2 - x)/(y**2 - y)
#    
#print g(15, 21)
#

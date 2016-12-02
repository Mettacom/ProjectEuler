def f(n):
    a=1
    b=2
    y=0
    while a<n:
        print(a)
        if a%2==0:
            y=y+a
        a,b=b,a+b
    print(y)
            
f(4000000)

f = {}

def fib(n):

    try:

        return f[n]

    except KeyError:

        if n <= 1:

            return n

        return fib(n-2) + fib(n-1)

n = 1

while True:

    fibn = fib(n)

    f[n] = fibn

    if fibn >= 10**999:

        print(n)

        break

    n += 1

import math, time

def isPrime(n):

    root = math.sqrt(n)

    for j in range(2, int(root) + 1):

        if n % j == 0:

            return False

    return True







def primes_below(n):

    ints = range(2, n)

    composites = []

    for i in ints:

        if i not in composites:

            for j in range(i, n, i):

                if j != i and j not in composites:

                    composites.append(j)




    compositeset = set(composites)

    intset = set(ints)

    primeset = intset.difference(compositeset)

    primes = list(primeset)

    primes.sort()

    return primes

def new_primes_below(n):

    ints = range(2, n)

    primes = []

    for i in ints:

        if isPrime(i):

            primes.append(i)

    return primes


start = time.time()
print(sum(new_primes_below(2000000)))
print("Using prime check:", time.time() - start, "seconds")

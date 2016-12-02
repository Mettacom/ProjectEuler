

def isPrime(n):

    root = n**0.5

    for j in range(2, int(root) + 1):

        if n % j == 0:

            return False

    return True

def quadratic(n, a, b):

    return n**2 + a*n + b


best = (0, 0)

numberofprimes = 0

for a in range(-1000, 1000):

    for b in range(-1000, 1000):

        n = 0

        testformula = []

        while quadratic(n, a, b) > 0:

            if isPrime(quadratic(n, a, b)):

                testformula.append(quadratic(n, a, b))

            else:

                break

            n += 1

        if len(testformula) > best[1]:

            best = (a*b, len(testformula))

            print(best)

print(best)

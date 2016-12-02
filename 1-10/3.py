def isPrime(n):

    root = n**0.5

    for j in range(2, int(root) + 1):

        if n % j == 0:

            return False

    return True

def p(n):

    factors = []

    for i in range(2, int(n/2) + 1):

        if n % i == 0 and isPrime(i):

            factors.append(i)

            print(i)

    return factors

print(p(600851475143))

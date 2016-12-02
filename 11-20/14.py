def collatz(n):

    t = [n]

    while n != 1:

        if n % 2 == 0:

            n //= 2

        else:

            n = 3*n + 1

        t.append(n)

    return(t)

cdict = {}

for n in range(1,1000000):

    cdict[n] = len(collatz(n))

k = list(cdict.keys())

v = list(cdict.values())

biggest = k[v.index(max(v))]

print(biggest)

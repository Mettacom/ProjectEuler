ddict = {1:[1], 2:[1,2]}

def d(n):

    total = [1]

    try:

        return sum(ddict[n])

    except KeyError:

        for i in range(2, n):

            if n % i == 0:

                total.append(i)

        ddict[n] = total

        return sum(ddict[n])

def a(n1, n2):

    return d(n1) == n2 and d(n2) == n1 and n1 != n2

total = 0

for i in range(2, 10000):

    for j in range(i, 10000):

        if a(i, j):

            total += i + j

            print(i, j)

print(total)

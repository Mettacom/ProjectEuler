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

alist = []

for i in range(12, 28123):

    if i not in alist and d(i) > i:

        alist.append(i)

print(alist)

nlist = []

for i in range(len(alist)):

    for j in range(i, len(alist)):

        if alist[i] + alist[j] <= 28123:

            nlist.append(alist[i] + alist[j])

print(nlist)

xlist = []

for n in range(1, 28123):

    if n not in nlist:

        print(n)

        xlist.append(n)

print(xlist)

print(sum(xlist))

n = 2**1000

nlist = [int(str(n)[i]) for i in range(len(str(n)))]

print sum(nlist)
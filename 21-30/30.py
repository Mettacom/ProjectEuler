import time

def sumofdigits(n, p=1):

    return sum([int(i)**p for i in list(str(n))])

def newsumofdigits(n, p=1, memo={}):
    
    if n in memo:
        return memo[n]
    nlist = list(str(n))
    if len(nlist)==1:
        return n**p
    fdigit = int(nlist[0])
    rdigits = [str(i) for i in nlist[1:]]
    nrdigits = int(''.join(rdigits))
    if nrdigits in memo:
        return memo[nrdigits]
    ans = (fdigit**p)+newsumofdigits(nrdigits, p, memo)
    memo[nrdigits] = ans
    return ans



total = 0
t = time.time()
for i in range(2,1000000):
    if sumofdigits(i, 5) == i:
        total += i
        print(i)
print(total, -t+time.time())

#total = 0
#t = time.time()
#for i in range(10000):
#    if newsumofdigits(i, 4) == i:
#        total += i
#print(total, -t+time.time())

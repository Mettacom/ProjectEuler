import string

f = open("/home/rey/Programming/Project Euler/21-30/p022_names.txt")

names = f.read().split('","')

names[0] = 'MARY'

names[-1] = 'ALONSO'

names.sort()

adict = {}

for i in range(1,27):

    adict[string.ascii_uppercase[i-1]] = i

runningtotal = 0

for i in range(len(names)):

    total = 0

    for a in names[i]:

        total += adict[a]

    runningtotal += total * (i+1)

print(runningtotal)

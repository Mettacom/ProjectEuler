import itertools as it


def p(s):

    return map(''.join, it.permutations(s))

s = '0123456789'



l = [int(i) for i in p(s)]

l.sort()

print(l[999999])

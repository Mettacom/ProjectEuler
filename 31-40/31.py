
memo = {}
coins = [1,2,3]

def numcoins(n, coins, memo):
    x=0
    if n in memo:
        return memo[n]
    elif n in coins:
        return 1
    for c in coins:
        if n-c>0:
            x += numcoins(n-c, coins, memo)
    if n not in memo:
        memo[n] = x
    return x

l = numcoins(4, coins, memo)
print(memo)

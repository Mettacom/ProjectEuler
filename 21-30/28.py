def spiralin(n):

    if n == 1:

        return 1

    return n**2 + (n**2-(n-2)-1) + (n**2-2*(n-2)-2) + (n**2-3*(n-2)-3) + spiralin(n-2)

print(spiralin(1001))

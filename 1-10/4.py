digits = (999, 100)

def isPalindrome(N):
    listN = list(str(N))
    reverseN = list(listN)
    reverseN.reverse()
    return listN == reverseN
def palindromeCheck(digits):
    palindromes = []
    for i in range(digits[0], digits[1], -1):
        for j in range(digits[0], digits[1], -1):
            if isPalindrome(i*j):
                palindromes.append(i*j)
    return max(palindromes)
print palindromeCheck(digits)

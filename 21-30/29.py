exponents = []

for i in range(2, 101):

    for j in range(2, 101):

        exponents.append(i**j)

print(len(set(exponents)))

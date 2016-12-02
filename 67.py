def get_triangle(filename):

    f = open(filename, 'r')

    l = f.read().split()

    for i in range(len(l)):

        if l[i][0] == '0':

            l[i] = l[i][1:]

        l[i] = int(l[i])

    triangle = []

    t = 0

    for i in range(1,101):

        triangle.append(l[t:t+i])

        t += i

    return triangle


def dynamic(i = 0, j = 0, memo = {}):

    l1 = triangle[i]

    l2 = triangle[i+1]

    try:

        return memo[(i, j)]

    except KeyError:

        total = triangle[i][j]

        if len(triangle[i:]) == 2:

            total += max(l2[j], l2[j+1])

            memo[(i, j)] = total

            return total

        total += max(dynamic(i+1, j, memo), dynamic(i+1, j+1, memo))

        memo[(i, j)] = total

        return total

triangle = get_triangle("/home/rey/Programming/Project Euler/p067_triangle.txt")

print(dynamic())

# print(triangle)

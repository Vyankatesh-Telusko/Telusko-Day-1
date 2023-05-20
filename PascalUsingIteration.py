def print_pascal_iterative(n):
    pascal_triangle = [[0] * (i + 1) for i in range(n)]

    for i in range(n):
        pascal_triangle[i][0] = 1
        pascal_triangle[i][i] = 1

        for j in range(1, i):
            pascal_triangle[i][j] = pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j]

    for row in pascal_triangle:
        print(' '.join(map(str, row)))

print_pascal_iterative(5)

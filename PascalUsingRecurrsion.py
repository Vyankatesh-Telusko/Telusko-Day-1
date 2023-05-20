def pascal_recursive(row, col):
    if col == 0 or col == row:
        return 1
    else:
        return pascal_recursive(row - 1, col - 1) + pascal_recursive(row - 1, col)

def print_pascal_recursive(n):
    for i in range(n):
        for j in range(i + 1):
            print(pascal_recursive(i, j), end=" ")
        print()

print_pascal_recursive(5)

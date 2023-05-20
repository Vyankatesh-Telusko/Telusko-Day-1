def pascal_memoization(row, col, memo):
    if col == 0 or col == row:
        return 1
    elif (row, col) in memo:
        return memo[(row, col)]
    else:
        result = pascal_memoization(row - 1, col - 1, memo) + pascal_memoization(row - 1, col, memo)
        memo[(row, col)] = result
        return result

def print_pascal_memoization(n):
    memo = {}
    for i in range(n):
        for j in range(i + 1):
            print(pascal_memoization(i, j, memo), end=" ")
        print()

print_pascal_memoization(5)

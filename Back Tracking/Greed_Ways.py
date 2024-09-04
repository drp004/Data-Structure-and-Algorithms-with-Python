def Ways(i, j, n, m):
    if i == n-1 and j == m-1:
        return 1
    if i == n or j == m:
        return 0

    return Ways(i + 1, j, n , m) + Ways(i, j + 1, n, m)


n = int(input("Enter n : "))
m = int(input("Enter m : "))
print(Ways(0, 0, n, m))
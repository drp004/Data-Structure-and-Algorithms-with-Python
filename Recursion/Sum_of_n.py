def sum(n):
    if n == 1:
        return 1

    return n + sum(n-1)

n = int(input("Enter num : "))
print(f"Sum of first {n} number is {sum(n)}")
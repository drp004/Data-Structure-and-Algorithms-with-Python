n = int(input("Enter N : "))
i = int(input("Enter i : "))
j = int(input("Enter j : "))

def clear_range(n, i, j):
    a = ~(0)<<j
    b = (1<<i) - 1

    return n & (a | b)

print("Updated number is :", clear_range(n, i, j))
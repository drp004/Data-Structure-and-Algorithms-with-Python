n = int(input("Enter N : "))
i = int(input("Enter i : "))

n = n & (~(0)<<i)

print("Updated number is :", n)
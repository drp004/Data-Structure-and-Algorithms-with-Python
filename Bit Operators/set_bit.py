n = int(input("Enter N : "))
i = int(input("Enter i : "))

bit = n | (1<<i)

print("Updated number is : ", bit)
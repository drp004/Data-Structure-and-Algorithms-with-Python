n = int(input("Enter N : "))
i = int(input("Enter i : "))

bit = n & (1<<i)

if bit == 0:
    print(f"{i}th bit is : 0")
else:
    print(f"{i}th bit is : 1")
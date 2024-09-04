n = int(input("Enter N : "))
i = int(input("Enter i : "))
up = int(input("Enter bit to Update : "))

if up == 0 :
    bit = n & ~(1<<i)
else :
    bit = n | (1<<i)

print("Updated number is :", bit)
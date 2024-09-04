n = int(input("Enter number : "))

def count_set_bit(n):
    count = 0
    while n > 0:
        if n & 1:
            count += 1

        n = n >> 1
    
    return count

print("Total set bit :", count_set_bit(n))
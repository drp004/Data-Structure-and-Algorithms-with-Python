n = int(input("Enter Num : "))
p = int(input("Enter power : "))

def power(n, p):
    ans = 1
    while p > 0:
        if p & 1 == 1 : 
            ans = ans * n

        n = n * n
        p = p >> 1

    return ans

print(power(n, p))
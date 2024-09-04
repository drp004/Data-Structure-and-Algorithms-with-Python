n = int(input("Enter Number : "))
p = int(input("Enter power : "))

def power(n, p):
    if p == 0:
        return 1
    
    return n * power(n, p-1)

def power_opt(n, p):
    if p == 0:
        return 1

    # for even power half power  (p//2 count) 
    halfpow = power_opt(n, p//2) * power_opt(n, p//2)
    
    # for odd power n * halfpower
    if p % 2 != 0:
        halfpow = n * halfpow

    return halfpow

print(f"{n} to the Power {p} : {power(n, p)}")
print(f"{n} to the Power {p} : {power_opt(n, p)}")
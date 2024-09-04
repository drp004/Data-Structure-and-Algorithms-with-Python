n = int(input("Enter number of friends : "))

def pairing(n):
    if n == 1 or n == 2:
        return n

    single = pairing(n-1)
    pair = (n-1) * pairing(n-2)

    return single + pair

print(pairing(n))
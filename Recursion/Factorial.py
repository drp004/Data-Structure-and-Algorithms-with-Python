def fac(n):
    if n == 0:
        return 1

    return n * fac(n-1)


n = int(input("Enter num : "))
print(f"factorial of {n} is {fac(n)}")
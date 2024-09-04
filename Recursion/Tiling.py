n = int(input("Enter Floor size : "))

def tiling(n):

    # base case
    if n == 0 or n == 1:
        return 1

    # vertical choice
    ver = tiling(n-1)

    #horizontal choice
    hor = tiling(n-2)

    ways = ver + hor

    return ways

print("Total tiling ways are :", tiling(n))
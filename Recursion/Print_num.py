# print number from 1 to n

def printnum(n):
    if n == 1:
        print(1)
        return 

    printnum(n-1)
    print(n)
    return

n = int(input("Enter num :"))
printnum(n)
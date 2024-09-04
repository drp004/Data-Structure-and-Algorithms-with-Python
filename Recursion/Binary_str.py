n = int(input("Enter N : "))

def Binary_Str(n):
    
    # Base Case
    if n == 0:
        return 1
    elif n == 1:
        return 2

    # choose 
    zero = Binary_Str(n-1)
    one = Binary_Str(n-2)

    return zero + one 

def Binary_String(n, lp, str):
    if n == 0:
        print(str)
        return 
    
    Binary_String(n-1, 0, str+"0")
    if lp == 0:
        Binary_String(n-1, 1, str+"1")

print("Total Binary Str :", Binary_Str(n))
str = ""
print("Total Binary Str :", Binary_String(n, 0, str))
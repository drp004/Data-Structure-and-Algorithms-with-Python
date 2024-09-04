n = int(input("Enter N : "))

def check_pow(n):
    if n & n-1 == 0:
        return True
    else:
        return False    

print(check_pow(n))        
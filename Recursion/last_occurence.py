arr = list(map(int, input("Enter Array Element : \n").split()))
key = int(input("Enter key : "))

def check_key(arr, idx, key):
    if idx == len(arr):
        return False
    if arr[idx] == key:
        return True
    
    return check_key(arr, idx+1, key)

def first_occurence(arr, idx, key):
    if idx == len(arr):
        return -1
    if arr[idx] == key:
        return idx
    
    return first_occurence(arr, idx+1, key)

def last_occurence(arr, idx, key):
    if idx < 0:
        return -1
    if arr[idx] == key:
        return idx
    
    return last_occurence(arr, idx-1, key)

print(f"Key is present : {check_key(arr, 0, key)}")
print(f"First Ocuurence of {key} is {first_occurence(arr, 0, key)}")
print(f"Last Ocuurence of {key} is {last_occurence(arr, len(arr)-1, key)}")
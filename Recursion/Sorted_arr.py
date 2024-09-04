arr = list(map(int, input("Enter Array Element : \n").split()))

def check_sorted(arr, idx):
    if idx ==  len(arr)-1:
        return True
    if arr[idx] > arr[idx+1]:
        return False

    return check_sorted(arr, idx+1)

print(check_sorted(arr, 0))
def arr_set(arr, n, val):
    if n == (len(arr)):
        print(arr)
        return

    arr[n] = val
    arr_set(arr, n+1, val+1)
    arr[n] = arr[n] - 1


l = int(input("Enter len : "))
val = int(input("Enter Value : "))
arr = [0] * l
arr_set(arr, 0, val)
print(arr)
def rec_bubbel(arr, n):
    if n == 1:
        return

    didSwap = 0

    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            didSwap = 1

    if didSwap == 0:
        return

    rec_bubbel(arr, n-1)

arr = [10, 42, 55, 24, 33, 16]
rec_bubbel(arr, len(arr))
print(arr)
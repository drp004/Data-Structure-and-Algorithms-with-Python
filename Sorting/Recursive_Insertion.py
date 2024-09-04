def rec_Insertion(arr, n):
    if n ==1:
        return

    max = 0
    for i in range(n):
        if arr[i] > arr[max]:
            max = i

    arr[max], arr[n-1] = arr[n-1], arr[max]

    rec_Insertion(arr, n-1)

arr = [5,4,3,2,1]
rec_Insertion(arr, len(arr))
print(arr)
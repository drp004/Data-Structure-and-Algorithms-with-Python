def quick_sort(lst, low, high):
    if low < high:
        # getting pivot index
        pIdx = partionIdx(lst, low, high)
        quick_sort(lst, low, pIdx-1)
        quick_sort(lst, pIdx+1, high)

# sort according pivot Index
def partionIdx(lst, low, high):
    pivot = lst[low]
    i = low
    j = high

    while i < j :
        # getting element greater than pivot
        while lst[i] <= pivot and i < high:
            i += 1
        # getting element less than pivot
        while lst[j] > pivot and j > low:
            j -= 1
        # swap elements
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]

        # swapping the pivot
        lst[low], lst[j] = lst[j], lst[low]

    return j

print("Enter List : ")
lst = list(map(int, input().split()))
quick_sort(lst, 0, len(lst)-1)
print("Sorted List : \n", lst)                         
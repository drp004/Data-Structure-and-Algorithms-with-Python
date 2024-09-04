def Selection_sort(lst):

    # for counting turn
    for i in range(len(lst)):
        minpos = i
        # for finding postion
        for j in range(i, len(lst)):
            if lst[minpos] > lst[j]:
                minpos = j
        # Swapping
        lst[i], lst[minpos] = lst[minpos], lst[i]
    return

print("Enter List :")
lst = list(map(int, input().split()))
Selection_sort(lst)
print("Sorted list :", lst)        
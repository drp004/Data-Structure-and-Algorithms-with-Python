def bubbel(lst):

    # for counting turn
    for i in range(len(lst)-1, 0, -1):
        # for swapping with adjcent element
        didSwap = 0
        for j in range(0, i):
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                didSwap = 1

        if didSwap == 1:
            break

    return

print("Enter a List :")
lst = list(map(int, input().split()))
print("Given Array :", lst)
bubbel(lst)
print("Sorted list :", lst) 
def isSorted(lst, i):
    if i == 0:
        return True
    if lst[i] < lst[i-1]:
        return False
    return True and isSorted(lst, i-1)

lst = [1, 3, 5, 7]
print(isSorted(lst, len(lst)-1))
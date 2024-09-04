lst = list(map(int, input("Enter list Elements : ").split()))

def mergeSort(lst):
    if len(lst)<=1:
        return lst

    mid = len(lst)//2

    left = mergeSort(lst[:mid])
    right = mergeSort(lst[mid:])

    return sort(left, right)
 
def sort(left, right):
    i = 0
    j = 0
    sorted = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1

    sorted += left[i:]
    sorted += right[j:]

    return sorted

lst = mergeSort(lst)
print(lst)
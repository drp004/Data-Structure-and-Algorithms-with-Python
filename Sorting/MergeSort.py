def merge_sort(lst):
    if len(lst)<=1:
        return lst

    # Dividing List
    mid = len(lst)//2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)

# Merge lists
def merge(left, right):
    result = []
    i = 0
    j = 0

    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

print("Enter List : ")
lst = list(map(int, input().split()))
lst = merge_sort(lst)
print("Sorted List : \n", lst)
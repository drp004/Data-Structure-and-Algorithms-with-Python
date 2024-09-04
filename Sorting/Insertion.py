def insertion(lst):

    for i in range(1, len(lst)):
        j = i
        # for finding correct postion
        while j > 0 and lst[j-1] > lst[j]:
            # placing at corret postion 
            lst[j], lst[j-1] = lst[j-1], lst[j]
            j -= 1


print("Enter a List :")
lst = list(map(int, input().split()))
print("Given Array :", lst)
insertion(lst)
print("Sorted Array :", lst)
def counting(lst):
    # finding max value
    maxval = max(lst)

    # making another arr with index upto maxvalue+1
    count = [0] * (maxval+1)
    for i in lst:
        count[i] += 1 

    #sorting
    j = 0
    for i in range(len(count)):
        while count[i] > 0:
            lst[j] = i
            count[i] -= 1
            j += 1

print("Enter a List :")
lst = list(map(int, input().split()))
print("Given Array :", lst)
counting(lst)
print("Sorted list :", lst) 
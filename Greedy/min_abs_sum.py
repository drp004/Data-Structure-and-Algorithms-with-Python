def min_abs_sum(a, b):
    a.sort()
    b.sort()

    sum = 0

    for i in range(len(a)):
        sum += abs(a[i]-b[i])

    return sum

a = [2,1,3]
b = [1,2,3]
print(min_abs_sum(a, b))
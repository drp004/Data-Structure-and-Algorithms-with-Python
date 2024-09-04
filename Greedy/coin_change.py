def min_change(Value, currency):
    currency.sort()

    i = len(currency)-1
    count = 0

    while i >= 0:
        if currency[i] <= Value:
            Value -= currency[i]
            print(currency[i], end=" ")
            count += 1
        else:
            i -= 1
    print(" ")

    return count

curr = [1,2,5,10,20,50,100,200,500,2000]
v = 1059
print(min_change(v, curr))
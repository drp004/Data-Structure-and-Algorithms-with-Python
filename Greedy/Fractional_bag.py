def frac_bag(value, weight, W):
    ratio = [value[i]//weight[i] for i in range(len(value))]
    
    items = [(ratio[i], i) for i in range(len(value))]
    items.sort()
    # print(items)
    cap = W
    total = 0

    for i in range(len(ratio)-1, -1, -1):
        if cap >= weight[items[i][1]]:
            total += value[items[i][1]]
            cap -= weight[items[i][1]]
        else:
            total += items[i][0] * cap
            cap -= weight[items[i][1]]

    return total

value = [60, 100, 120]
weight = [10, 20, 30]
W = 50
print(frac_bag(value, weight, W))
def MaxChain(pairs):
    pairs.sort(key=lambda x:x[1])
    print(pairs)

    chainEnd = pairs[0][1]
    count = 1

    for i in range(len(pairs)):
        if pairs[i][0] > chainEnd:
            chainEnd = pairs[i][1]
            count += 1

    return count


pairs = [[5, 24],[39, 60], [5, 28], [27, 40], [50, 90]]
print(MaxChain(pairs))
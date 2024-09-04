start = [1,3,0,5,8,5]
end = [2,4,6,7,9,9]

# if Arra of end time is not sorted then
# arr = [(end[i], start[i]) for i in range(len(end))]
# arr.sort()

def max_act(start, end):
    ans = []

    maxAct = 1
    ans.append(0)
    endtime = end[0]

    for i in range(1, len(start)):
        if start[i] >= endtime:
            maxAct += 1
            ans.append(i)
            endtime = end[i]

    print('Max Activity :', maxAct)
    print(ans)

max_act(start, end)
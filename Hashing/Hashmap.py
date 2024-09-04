from collections import defaultdict

def count(arr):
    mpp = defaultdict(int)

    # Building hash map using dictionary
    for i in arr:
        mpp[i] += 1

    # printing element count
    for i in mpp:
        print(f"{i} occures {mpp[i]} times.")

arr = [1, 2, 3, 1, 2]
count(arr)
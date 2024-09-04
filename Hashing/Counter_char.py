from collections import Counter

st = "abbcdeccabe"

# Creating Counter hashmap
cnt = Counter(st)    # O(n)

print(cnt)
print(cnt['a'])
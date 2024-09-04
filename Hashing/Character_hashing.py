st = input("Enter String : ")

hash = [0]*26       # if Capital and small both are allowed then use 255 length. and assign at s[i]
for i in range(len(st)):
    hash[ord(st[i])-ord('a')] += 1

target = input("Enter Target character String : ")
for i in target:
    print(f"{i} occurece {hash[ord(i) - ord('a')]} times.")
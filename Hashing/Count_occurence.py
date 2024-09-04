# Count Occurence of : 1,2,3,4,12 
n = int(input("Enter Array Length :"))
arr = list(map(int, input("Enter Array Elements :").split()))

hash = [0]*13
for i in range(n):
    hash[arr[i]] += 1

target = list(map(int, input("Enter Targets :").split()))

for i in target:
    print(f"{i} occurence {hash[i]} times.")
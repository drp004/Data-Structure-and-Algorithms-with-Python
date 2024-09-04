def subsets(str, s, idx):
    if idx == len(str):
        print(s)
        return 

    subsets(str, s+str[idx], idx+1)
    subsets(str, s, idx+1)

str = input("Enter String : ")
subsets(str, '', 0)
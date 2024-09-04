'''
Pascal's Triangle :  numRows = 5  genrated_lst = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]    
            1   
           1 1
          1 2 1
         1 3 3 1
        1 4 6 4 1    
'''    

def genrate(numRows):           # Itrative Approach
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1],[1,1]]

    n = 3
    lst = [[1],[1,1]]
    while n <= numRows:
        l=[]
        for i in range(0, n):
            if i == 0 or i == (n-1):
                l.append(1)
            else:
                l.insert(i, lst[n-2][i-1]+lst[n-2][i])
        lst.append(l)    
        n += 1

    return lst

def genrate_rec(numRows):       # Recursive Approach
    if numRows == 1:
        return [[1]]

    prev = genrate_rec(numRows-1)
    lst = [1] * numRows

    for i in range(1, numRows-1):
        lst[i] = prev[-1][i-1] + prev[-1][i]

    prev.append(lst)
    return prev        


n = int(input("Enter Number of Rows : "))
li = genrate(n)
print("Itrative Approach :", li)
lr  = genrate_rec(n)
print("Recursive Approach :", lr)
def getTri(A):
    if A == 0:
            return [[1]]
    elif A == 1:
        return [[1],[1, 1]]

def getRow(A):
        ptri = getTri(A-1)
        ls = [1]*(A+1)
        for i in range(1, A):
            ls[i] = ptri[-1][i-1] + ptri[-1][i]
            
        return ls

print(getRow(3))
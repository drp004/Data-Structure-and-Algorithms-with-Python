'''
Pascal's Triangle :  rowindex = 4  genrated_lst = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]    
            1                  index : 0
           1 1                         1
          1 2 1                        2
         1 3 3 1                       3
        1 4 6 4 1                      4
'''    

def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    pascalTriangle = [[1]*(i+1) for i in range(rowIndex+1)]
    for row in range(2, rowIndex+1):
        for col in range(1, row):
            pascalTriangle[row][col] = pascalTriangle[row-1][col-1] + pascalTriangle[row-1][col]
    return pascalTriangle[rowIndex]

row_lst = getRow(3)
print(row_lst)
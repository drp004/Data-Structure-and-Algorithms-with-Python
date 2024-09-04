def isValid(s):
        lst = []
        for i in s:
            if i in "([{":
                lst.append(i)
            else :
                if (i==")" and lst[-1]=="(") or (i=="]" and lst[-1]=="[") or (i=="}" and lst[-1]=="{"):  
                    lst.pop()
                else:
                    return False
        if len(lst):
            return False        
        return True

print(isValid("(]"))        

str = input("Enter String : ")

def RmDuplicate(str, s, idx, track):
    if idx == len(str):
        return s  

    if track[ord(str[idx]) - ord('a')] == 0:
        track[ord(str[idx]) - ord('a')] = 1
        s += str[idx]

    return RmDuplicate(str, s, idx+1, track)
    
track = [0] * 26
print(RmDuplicate(str, "", 0, track)) 
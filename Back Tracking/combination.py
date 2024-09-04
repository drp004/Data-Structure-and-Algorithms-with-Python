def combination(str, s):
    if len(str) == 0:
        print(s)
        return

    for i in range(len(str)):
        char = str[i]
        newstr = str[0:i] + str[i+1:]

        combination(newstr, s+char)

str = input("Enter String : ")
combination(str, "")
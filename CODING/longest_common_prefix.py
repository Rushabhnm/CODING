def longestCommonPrefix(strs):
    y = ""

    for i in range(0,len(strs[0])):
        for string in strs:
            if i==len(string) or string[i] != strs[0][i]:
                return y
        y += strs[0][i]

    return y
        
print(longestCommonPrefix(["flower","flow","flew"]))
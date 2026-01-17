def longestCommonPrefix(strs):
    if not strs:
        return ""
    common_prefix = strs[0]
    for string in strs[1:]:
        while not string.startswith(common_prefix):
            common_prefix = common_prefix[:-1]
            if common_prefix == "":
                return ""
    return common_prefix
    # for i in range(len(strs[0])):
    #     char = strs[0][i]
    #     for s in strs:
    #         if i >= len(s) or s[i] != char:
    #             return strs[0][:i]
    # return strs[0]

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
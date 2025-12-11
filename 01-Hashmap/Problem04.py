# 49 Group Anagrams

def GroupAnagrams(strs):
    chmapTostring = {}
    for s in strs:
        chmap = [0]*26
        for ch in s:
            chmap[ord(ch)-ord('a')] += 1
        key = tuple(chmap)
        if key in chmapTostring:
            chmapTostring[key] += [s]
        else:
            chmapTostring[key] = [s]
    return list(chmapTostring.values())



strs = ["eat","tea","tan","ate","nat","bat"]
print(GroupAnagrams(strs))


# time = (mn)
# space = (m)
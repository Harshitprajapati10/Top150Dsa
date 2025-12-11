#242 valid Anagram

def isAnagram(s,t):
    if len(s)!=len(t): return False
    countmap = [0]*26

    for i in s:
        countmap[ord(i)-ord('a')] += 1
    for j in t:
        countmap[ord(j)-ord('a')] -= 1
        if countmap[(ord(j)-ord('a'))] < 0:
            return False
    return True

print(isAnagram("anagram","nagaram"))
print(isAnagram("rat","car"))


# time N
# space O(26)
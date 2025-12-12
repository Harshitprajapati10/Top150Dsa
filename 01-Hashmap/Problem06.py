# Encode and decode strings

#["lint", "code", "love", "you"]
# 4#lint4#code4#love3#you // length followed by string

def encode(strs):
    embedding = ""
    for s in strs:
        embedding += (f"{len(s)}" + "#" + s)
    return embedding

def decode(s):
    res = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        start = j + 1
        end = start + length
        res.append(s[start:end])
        i = end
    return res

s = ["lint", "code", "love", "you"]
print(encode(s))
print(decode(encode(s)))    
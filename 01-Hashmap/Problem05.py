# 347 Top k frequent elementst 

def topKfrequentElements(nums,k):
    count = {}
    for n in nums:
        count[n] = count.get(n,0)+1
    freq = [[] for i in range(len(nums)+1)]
    for n,c in count.items():
        freq[c].append(n)
    
    res = []
    for i in range(len(freq)-1,0,-1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
    return res

nums = [1,2,1,2,1,2,3,1,3,2]
k = 2

print(topKfrequentElements(nums, k))
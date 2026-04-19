# smallest stable index
# 3903,3904

nums = [5,0,1,4]
k = 3

# Output: 3


def firststableindex(nums, k):
    maxonleft = nums[0]
    for i in range(0,len(nums)):
        maxonleft = max(maxonleft,nums[i])
        minonright = min(nums[i:])
        if (maxonleft - minonright) <= k: return i
    return -1

print(firststableindex(nums, k))
print(firststableindex([3,2,1], 1))
print(firststableindex([0], 0))
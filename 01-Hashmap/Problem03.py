# Two sum

def Twosum(nums, target):
    hashset = {}
    for i,n in enumerate(nums):
        if target-n in hashset:
            return [hashset[target-n], i]
        hashset[n] = i
    return [-1,-1]

nums = [2,7,11,15]
target = 9
print(Twosum(nums,target))

# T N
# S N
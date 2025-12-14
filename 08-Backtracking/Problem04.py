# 46 permutations

nums = [1,2,3]

def permute(nums):
    if len(nums) == 1: return [nums]
    result = []
    for i, num in enumerate(nums):
        remaining_nums = nums[:i] + nums[i+1:]
        for perm in permute(remaining_nums):
            result.append([num] + perm)
    return result

print(permute(nums))
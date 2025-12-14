# 78 subsets

nums = [1,2,3]

def subsets(nums):
    result = []
    
    def backtrack(start, path):
        result.append(path)
        for i in range(start, len(nums)):
            backtrack(i + 1, path + [nums[i]])
    
    backtrack(0, [])
    return result

print(subsets(nums))  # Expected output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
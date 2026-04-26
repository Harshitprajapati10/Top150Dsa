# find subarray sum 

nums = [3,1,4,9,2,1,7,5]
targetSum = 10
# output = [s,e] indices, [4,6]

def subarray_sum(nums, targetSum):
    curr_sum = nums[0]
    i, j = 0, 1
    while j<len(nums):
        if curr_sum < targetSum:
            curr_sum += nums[j]
            j+=1
        elif curr_sum > targetSum:
            curr_sum -= nums[i]
            i+=1
        else:
            return [i,j-1]
    return [-1,-1]


print(subarray_sum(nums, targetSum))




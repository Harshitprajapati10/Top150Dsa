# longest subarray sum

nums = [4,3,3,2,1,5,2,3,5,10,1]
targetsum = 10
# out = 4 as [2,1,5,2] is longest


def longest_subarray_sum(nums, targetSum):
    if not nums:
        return 0
    curr_sum = nums[0]
    i, j = 0, 1
    longest_sub_len = 0
    while j<=len(nums):
        if curr_sum < targetSum:
            curr_sum += nums[j]
            j+=1
        elif curr_sum > targetSum:
            curr_sum -= nums[i]
            i+=1
        if curr_sum == targetSum:
            longest_sub_len = max(longest_sub_len, j-i+1)
            i+=1
            j+=1
    return longest_sub_len

print(longest_subarray_sum(nums, targetsum))
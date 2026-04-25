# subarray target sum size k

nums = [2,3,2,2,3,1,3,8,5,0,2,4]
target = 7
k = 3

def max_sum(nums,target, k):
     n = len(nums)
     curr_sum = sum(nums[:k])
     count = 1 if curr_sum == target else 0
     for i in range(k,n):
          curr_sum += nums[i] - nums[i-k]
          if curr_sum == target: count+= 1
     return count

print(max_sum(nums, target, k))
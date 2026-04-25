# max subarray sum size k

nums = [1,4,1,10,25,3,5,0,26]


def max_sum_helper(nums, i, j):
    c_sum = 0
    while i<=j:
        c_sum += nums[i]
        i+=1
    return c_sum

def max_sum_k(nums, k): # O(nk)
        i, j = 0, k-1
        max_sum = 0
        while j<len(nums):
            if nums[i] != nums[i+1] and nums[j] != nums[j-1]:
                max_sum = max(max_sum, max_sum_helper(nums,i,j))
            # print(i,j)
            i+=1
            j+=1
        return max_sum


def max_sum_k_optimized(nums, k): # O(n)
     curr_sum = 0
     for a in range(k):
          curr_sum += nums[a]
     max_sum = 0
     i, j = 0, k
     while j<len(nums):
   
          curr_sum -= nums[i] 
          curr_sum += nums[j]
          max_sum = max(max_sum,curr_sum)
        #   print(max_sum)
          i+=1
          j+=1
     return max_sum

def max_sum_pythonic(nums, k):
     n = len(nums)
     curr_sum = sum(nums[:k])
     max_sum = curr_sum
     for i in range(k,n):
          curr_sum += nums[i] - nums[i-k]
          max_sum = max(curr_sum, max_sum)
     return max_sum
          
res = max_sum_pythonic([1,4,1,10,25,3,5,0,26],4)
print(res)
print(max_sum_pythonic([1,5,4,2,9,9,9],3))
# print(max_sum_k(nums = [4,4,4], k = 3))
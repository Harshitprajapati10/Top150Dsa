# max product subarray size k

def max_product_subarray(nums, k):
    n = len(nums)
    curr_prod , max_prod = 1,0
    for i in range(0,n-k+1):
        j = i+k
        for l in range(i, j): curr_prod *= nums[l]
        max_prod = max(max_prod, curr_prod)
        curr_prod = 1
    return max_prod

def max_product_subarray_optimized(nums, k):
    n = len(nums)
    if n < k: return None
    curr_prod = 1
    for i in range(k):curr_prod *= nums[i]
    max_prod = curr_prod
    for i in range(k, n):
        incoming = nums[i]
        outgoing = nums[i - k]
        if outgoing != 0: curr_prod = (curr_prod // outgoing) * incoming
        else:
            curr_prod = 1
            for j in range(i - k + 1, i + 1):
                curr_prod *= nums[j]
        max_prod = max(max_prod, curr_prod)
    return max_prod

print(max_product_subarray_optimized([1,4,1,6,-3,3,-5,2,26], 4))
print(max_product_subarray_optimized([0,0,0,4,3,0,4,0,0,0], 2))

# 238 product of array except self


def productExceptSelf(nums):
        # 1,2,3,4
        # 1,1,2,6 trav
        # 24,12,8,6
        l,r = 1,1
        trav = [1]*len(nums)
        for i in range(len(nums)):
            trav[i] *= l
            l *= nums[i]
        print(trav)
        for j in range(len(nums)-1,-1,-1):
            trav[j] *= r
            r *= nums[j]
        return trav


print(productExceptSelf([1,2,3,4]))
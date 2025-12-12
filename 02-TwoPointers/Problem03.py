# three sum

nums = [-1,0,1,2,-1,-4] # vals that sum upto 0


def threeSum(nums):
    res = []
    nums.sort()
    # print(nums)
    for i in range(len(nums)):
        s = i+1
        e = len(nums)-1
        while(s<e):
            key = nums[i] + nums[s] + nums[e]
            if key == 0:
                res.append([nums[i], nums[s], nums[e]])
                s+=1
                e-=1
            elif key<0:
                s+=1
            else:
                e-=1
    return [list(t) for t in set(tuple(x) for x in res)]


print(threeSum(nums))
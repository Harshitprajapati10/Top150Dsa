# Two sum 2 

numbers = [2,7,11,15]
target = 9

def two_sum(nums,target):
    s,e = 0, len(nums)-1
    while(s<=e):
        if nums[s] + nums[e] == target:
            return [s,e]
        elif nums[s] + nums[e] < target:
            s+=1
        else:
            e-=1
    return [-1,-1]

print(two_sum(numbers,target))

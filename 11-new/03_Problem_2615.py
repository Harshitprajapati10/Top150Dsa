# 2615 sum of distaces

from collections import defaultdict
from itertools import accumulate
from typing import List


nums = [1,3,1,1,2]
# Output: [5,0,3,4,0]

def distance(nums):
    res = [0]*len(nums)
    for i in range(len(nums)):
        i_sum = 0
        for j in range(len(nums)):
            if j!=i and nums[j] == nums[i]:
                i_sum += abs(i-j)
        res[i] = i_sum
    return res

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        lsts,prfs,idxs = defaultdict(list), dict(), [0]*len(nums)
        for i,num in enumerate(nums): idxs[i] = len(lsts[num]); lsts[num].append(i)
        for num,lst in lsts.items():  prfs[num] = [*accumulate(lst, initial=0)]
        return [
            i *(2*idxs[i] -len(lsts[num])) +prfs[num][-1] - 2*prfs[num][idxs[i]]
            for i,num in enumerate(nums)
        ]

print(distance(nums))

o = Solution()
print(o.distance(nums))
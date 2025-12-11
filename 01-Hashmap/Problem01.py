# 217 -> contains duplicate
from typing import List

def containsDuplicate(nums: List[int]) -> bool:
        hash_set = {}
        for n in nums:
            if n in hash_set:
                return True
            else:
                hash_set[n] = 1
        return False

print(containsDuplicate([1,2,3,4]))
print(containsDuplicate([1,2,3,1]))


"""
Time = N
space = N
"""
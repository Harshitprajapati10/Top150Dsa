# 40 cmbination sum two

# use value one at a time, return all combs

candidates = [10,1,2,7,6,1,5]
target = 8

def combinationsum(candidates, target):
    candidates.sort()
    res = []

    def backtrack(start, curr, curr_sum):
        if curr_sum == target:
            res.append(curr[:])
            return
        if curr_sum > target:
            return
            

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            curr.append(candidates[i])
            backtrack(i+1, curr, curr_sum + candidates[i])  # reuse allowed
            curr.pop()

    backtrack(0, [], 0)
    return res

print(combinationsum(candidates, target))
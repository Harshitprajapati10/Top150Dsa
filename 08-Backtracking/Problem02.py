 # 39 combination sum

candidates = [2,3,5]
target = 8

def combinationSum(candidates, target):
    res = []

    def backtrack(start, curr, curr_sum):
        if curr_sum == target:
            res.append(curr[:])
            return
        if curr_sum > target:
            return

        for i in range(start, len(candidates)):
            curr.append(candidates[i])
            backtrack(i, curr, curr_sum + candidates[i])  # reuse allowed
            curr.pop()

    backtrack(0, [], 0)
    return res


print(combinationSum(candidates, target))
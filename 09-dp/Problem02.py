# Min cost climbing stairs
# 746

cost = [10,15,20]

    #            .
    #          /     \
    #        /        \
    #       10        15
    #     /   \      /  \
    #   15     20    20   


def minCostClimbingStairs(cost):
    memo = {}
    return min(helper(cost, 0, memo),helper(cost, 1, memo))

def helper(cost, i, memo):
    if i >= len(cost):
        return 0
    if i in memo:
        return memo[i]
    first = cost[i] + helper(cost, i+1, memo)
    second = cost[i] + helper(cost, i+2, memo)
    memo[i] = min(first, second)
    return memo[i]

def minCostClimbingStairs_tabulation(cost):
    prev2 = cost[0]
    prev1 = cost[1]

    for i in range(2, len(cost)):
        curr = cost[i] + min(prev1, prev2)
        prev2 = prev1
        prev1 = curr

    return min(prev1, prev2)

print(minCostClimbingStairs(cost))
print(minCostClimbingStairs_tabulation(cost))

    

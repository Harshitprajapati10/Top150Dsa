# 0-1 knapstack problem

"""
You are given n items, where each item has:a weight 
a value 

You are also given a knapsack with a maximum weight capacity  𝑊
Your task is to determine the maximum total value that can be obtained by selecting a subset of the items such that:

the total weight of selected items does not exceed 
𝑊

each item can be either included once or not included at all
"""

# example
weights = [2,1,3,2]
values = [12,10,20,15]
W = 5

# ans = "1011" # maxVal = 37


# --------------
# WAY 1 - GREEDY
# sort on basis of values
# pick highest value and put in knapstack
def greedy_knapstack(weights, values, W):
    items = list(zip(values,weights)) # [(v,w),(v,w)]
    items.sort(key = lambda x :x[0], reverse=True)
    sorted_values, sorted_weights = zip(*items)
    weights = list(sorted_weights)
    values = list(sorted_values)
    # wei = [3,  2,  2,  1]
    # val = (20, 15, 12, 10)
    capacity = W
    maxVal = 0
    for i,val in enumerate(values):
        if weights[i] <= capacity:
            maxVal += val
            capacity = capacity - weights[i]
    return maxVal


#------------------
# dp recursion

def recursive_knapstack(weights, values, W):

    def dfs(i, capacity):
        if i == len(values) or capacity == 0: # no item left
            return 0
        if weights[i]>capacity:# skip the item
            return dfs(i+1, capacity)
        # not take the item
        not_take = dfs(i + 1, capacity)
        # take the item
        take = values[i] + dfs(i + 1, capacity - weights[i])
        return max(take,not_take)

    print(dfs(0,W) )


def knapsack_with_path(weights, values, W):

    def dfs(i, capacity):
        if i == len(values):
            return 0, ""
        # option 1: not take
        val0, path0 = dfs(i + 1, capacity)
        val0_path = (val0, "0" + path0)
        # option 2: take (if possible)
        if weights[i] <= capacity:
            val1, path1 = dfs(i + 1, capacity - weights[i])
            val1 += values[i]
            val1_path = (val1, "1" + path1)
        else:
            val1_path = (-1, "")
        # choose the better option
        if val1_path[0] > val0_path[0]:
            return val1_path
        else:
            return val0_path

    maxVal, decision = dfs(0, W)
    return decision, maxVal


# -------------
# dp tabulation

def tabulation_knapstack(weights, values, W):
    n = len(weights)
    dp = [[0 for _ in range(W+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(W+1):
            if i==0 or j==0:
                dp[i][j] = 0
            else:
                pick = 0
                if weights[i-1] <= j:
                    pick = values[i-1]+ dp[i-1][j-weights[i-1]]
                
                notPick = dp[i-1][j]
                dp[i][j] = max(pick, notPick)

    return dp[n][W]


def tabulation_knapsack_with_binary(weights, values, W):
    n = len(weights)
    
    # build dp table
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(W + 1):
            notPick = dp[i - 1][j]
            pick = 0
            if weights[i - 1] <= j:
                pick = values[i - 1] + dp[i - 1][j - weights[i - 1]]
            dp[i][j] = max(pick, notPick)

    # backtracking to get binary string
    i, j = n, W
    binary = []

    while i > 0:
        if dp[i][j] == dp[i - 1][j]:
            binary.append('0')
        else:
            binary.append('1')
            j -= weights[i - 1]
        i -= 1

    binary.reverse()
    return "".join(binary), dp[n][W]



print(greedy_knapstack(weights=weights, values=values, W = W)) #35
recursive_knapstack(weights, values, W)# 37
print(knapsack_with_path(weights, values,W))
print(tabulation_knapstack(weights, values, W))
print(tabulation_knapsack_with_binary(weights, values, W))




# 70 climbing stairs

n = 5
# out 0 1 1 2 3 5, fib(n+1)

def get_ways(n):
    return fib(n+1)

def fib(n, memo={}):
    if n in memo: return memo[n]
    if n<2: return n
    memo[n] = fib(n-1)+fib(n-2)
    return memo[n]

print(get_ways(n))

# time N
# space depends
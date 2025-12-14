# 22 generate parenthesis

n = 3
# ["((()))","(()())","(())()","()(())","()()()"]

def generateParenthesis(n):
    result = []

    def backtrack(curr, open_count, close_count):
        if len(curr) == 2*n:
            result.append(curr)
            return
        
        # add '(' if we can
        if open_count<n:
            backtrack(curr+"(", open_count+1, close_count)
        
        # add ')' only if it is valid
        if close_count < open_count:
            backtrack(curr + ")", open_count, close_count+1)
    
    backtrack("",0,0)
    return result

print(generateParenthesis(5))
# 131 palindrome partitioning

s = "aab"
# Output: [["a","a","b"],["aa","b"]]

def partition(s):
    res = []

    def isPalindrome(sub):
        return sub == sub[::-1]

    def backtrack(start, path):
        # if we've used the whole string
        if start == len(s):
            res.append(path[:])
            return

        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]

            if isPalindrome(substring):
                path.append(substring)
                backtrack(end, path)
                path.pop()   # backtrack

    backtrack(0, [])
    return res


print(partition(s))
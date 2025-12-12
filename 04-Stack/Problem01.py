# 20 valid parentheses

s = "()[]{}"
t = "([{}])"
u = "([{])}"

def isValid(s):
    stack = []
    match = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack or stack[-1] != match[ch]:
                return False
            stack.pop()

    return len(stack) == 0
print(isValid(s))
print(isValid(t))
print(isValid(u))


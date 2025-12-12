# 150 Evaluate reverse polist notation
tokens = ["4","13","5","/","+"]
tokens1 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

def evalRPN(tokens):
    stack = []
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: int(a / b)
    }
    for ch in tokens:
        if ch.lstrip("-").isdigit():
            stack.append(int(ch))
        else:
            second = stack.pop()
            first = stack.pop()
            stack.append(operations[ch](first,second))
    return stack[-1]

print(evalRPN(tokens))
print(evalRPN(tokens1))
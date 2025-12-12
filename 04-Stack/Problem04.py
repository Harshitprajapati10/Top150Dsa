# 739-> daily tempreatures

temperatures = [73,74,75,71,69,72,76,73]

def dailyTemperatures(temperatures):
    stack = []
    res = [0]*len(temperatures)
    for i,t in enumerate(temperatures):
        while stack and t > temperatures[stack[-1]]:
            prev = stack.pop()
            res[prev] = i-prev
        stack.append(i)
    return res

print(dailyTemperatures(temperatures))
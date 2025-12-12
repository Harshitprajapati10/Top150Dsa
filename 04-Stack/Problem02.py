class MinStack:

    def __init__(self):
        self.S = []
        self.topv = -1

    def push(self, val: int) -> None:
        self.S.append(val)
        self.topv += 1

    def pop(self) -> None:
        if self.topv == -1:
            return
        self.S.pop()
        self.topv -= 1

    def top(self) -> int:
        if self.topv == -1:
            return None
        return self.S[self.topv]

    def getMin(self) -> int:
        if self.topv == -1:
            return None
        return min(self.S)


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(21)
obj.push(11)
obj.push(221)
obj.push(22)
obj.pop()
param_3 = obj.top()
print(param_3)
param_4 = obj.getMin()
print(param_4)
class MinStack:

    def __init__(self):
        self.stack = []
        self.current_min = None

    def push(self, val: int) -> None:
        if not self.stack:
            current_min = val
        else:
            minVal = self.stack[-1][1]
            current_min = min(minVal, val)
        self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

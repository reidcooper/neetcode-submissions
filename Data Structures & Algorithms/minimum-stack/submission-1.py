class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        m = None
        for el in self.stack:
            if m == None:
                m = el
                continue
                
            m = min(el, m)
        
        return m
        

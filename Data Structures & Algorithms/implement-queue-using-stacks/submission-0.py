class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        while self.stack2:
            pop_num = self.stack2.pop()
            self.stack1.append(pop_num)
        self.stack1.append(x)
        while self.stack1:
            pop_num = self.stack1.pop()
            self.stack2.append(pop_num) 
    def pop(self) -> int:
        return self.stack2.pop()

    def peek(self) -> int:
        return self.stack2[-1]
        

    def empty(self) -> bool:
        return not self.stack2
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
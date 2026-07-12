class StockSpanner:

    def __init__(self):
        self.stack = []
        self.buffer = []
    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append(price)
            return 1
        else:
            count = 1
            while self.stack and price >= self.stack[-1]:
                count += 1
                pop_num = self.stack.pop()
                self.buffer.append(pop_num)
            while self.buffer:
                pop_num = self.buffer.pop()
                self.stack.append(pop_num)
            self.stack.append(price)
            return count



        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
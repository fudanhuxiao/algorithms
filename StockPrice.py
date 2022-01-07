class StockPrice:

    def __init__(self):
        self.prices = {}
        self.maxtime = -1
        self.maxval = []
        self.minval = []

    def update(self, timestamp: int, price: int) -> None:
        self.prices[timestamp] = price
        self.maxtime = max(self.maxtime, timestamp)
        heappush(self.maxval, (-price, timestamp))
        heappush(self.minval, (price, timestamp))
        
    def current(self) -> int:
        return self.prices[self.maxtime]

    def maximum(self) -> int:
        while self.maxval and self.prices[self.maxval[0][1]] != -self.maxval[0][0]:
            heappop(self.maxval)
        return -self.maxval[0][0]

    def minimum(self) -> int:
        while self.minval and self.prices[self.minval[0][1]] != self.minval[0][0]:
            heappop(self.minval)
        return self.minval[0][0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()

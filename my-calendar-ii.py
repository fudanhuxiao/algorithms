class MyCalendarTwo:

    def __init__(self):
        self.calendar = []
        self.doublebooked = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.doublebooked:
            # De Morgan's laws
            if start < e and s < end:
                return False
        for s, e in self.calendar:
            if start < e and s < end:
                self.doublebooked.append([max(start, s), min(end, e)])
        self.calendar.append([start, end])
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)

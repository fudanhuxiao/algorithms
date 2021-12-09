class FreqStack:

    def __init__(self):
        self.freq = {}
        self.groups = defaultdict(list)
        self.maxfreq = 0

    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val,0)+1
        self.groups[self.freq[val]].append(val)
        self.maxfreq = max(self.maxfreq, self.freq[val])        

    def pop(self) -> int:
        val = self.groups[self.maxfreq].pop()
        self.freq[val] -= 1
        if not self.groups[self.maxfreq]:
            self.maxfreq -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

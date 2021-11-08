class Solution:
    def nextClosestTime(self, time: str) -> str:
        nums = set()
        for n in time:
            if n != ':':
                nums.add(n)
        combinations = []
        for a in nums:
            for b in nums:
                combinations.append(a+b)
        combinations.sort()
        def nextTime(limit, curTime, combinations):
            for i in range(len(combinations)):
                if combinations[i] == curTime:
                    if i == len(combinations)-1 or combinations[i+1] >= limit:
                        return combinations[0]
                    return combinations[i+1]
        nextMM = nextTime('60', time[3:], combinations)
        if nextMM > time[3:]:
            return time[:3]+nextMM
        return nextTime('24', time[:2], combinations)+':'+nextMM

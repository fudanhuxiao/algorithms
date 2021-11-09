class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        longest, prev = 0, -1
        for i in range(len(seats)):
            if seats[i] == 1:
                if prev == -1:
                    longest = i
                else:
                    longest = max(longest, (i-prev)//2)
                prev = i
        return max(longest, len(seats)-prev-1)

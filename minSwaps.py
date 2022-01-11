class Solution:
    def minSwaps(self, data: List[int]) -> int:
        total_ones = sum(data)
        max_ones, window_ones = 0, 0
        left = 0
        for right in range(len(data)):
            window_ones += data[right]
            if right >= total_ones:
                window_ones -= data[left]
                left += 1
            max_ones = max(max_ones, window_ones)
        return total_ones-max_ones

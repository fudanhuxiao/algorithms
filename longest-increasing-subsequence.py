class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subsequence = []
        for n in nums:
            if not subsequence or n > subsequence[-1]:
                subsequence.append(n)
            else:
                start, end = 0, len(subsequence)-1
                while start + 1 < end:
                    mid = (start+end)//2
                    if subsequence[mid] < n:
                        start = mid+1
                    else:
                        end = mid
                i = start if subsequence[start] >= n else end
                subsequence[i] = n
        return len(subsequence)

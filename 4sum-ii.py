class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        freq = {}
        lists = [nums1, nums2, nums3, nums4]
        def addToMap(i, key):
            if i == len(lists)//2:
                freq[key] = freq.get(key,0)+1
                return
            for n in lists[i]:
                addToMap(i+1, key+n)
        def findCounter(i, counter):
            if i == len(lists):
                return freq.get(counter, 0)
            ans = 0
            for n in lists[i]:
                ans += findCounter(i+1, counter-n)
            return ans
        addToMap(0, 0)
        return findCounter(len(lists)//2, 0)

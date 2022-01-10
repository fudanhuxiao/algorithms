class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counter1, counter2, left1, left2 = {}, {}, 0, 0
        ans = 0
        
        def moveLeft(counter, left, limit):
            while len(counter) > limit:
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                left += 1
            return left
        
        for right in range(n):
            num = nums[right]
            counter1[num] = counter1.get(num, 0)+1
            counter2[num] = counter2.get(num, 0)+1
            left1 = moveLeft(counter1, left1, k)
            left2 = moveLeft(counter2, left2, k-1)
            ans += left2-left1
        return ans

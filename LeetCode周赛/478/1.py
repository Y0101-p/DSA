from typing import List
class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        if k==0:
            return len(nums)
        nums.sort()
        cnt = 1
        n = len(nums)
        prev = nums[-1]
        for i in range(1,n):
            if nums[-1-i]<prev:
                prev = nums[-1-i]
                if cnt >= k:
                    break
            cnt += 1
        return n - cnt


sol = Solution()
nums = [5,5,5]
k = 1
print(sol.countElements(nums, k))
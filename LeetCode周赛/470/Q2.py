from typing import List
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        pr=nums[0]
        if pr!=0:
            judge=False
        else:
            judge=True
        for i in nums[1:]:
            pr=pr^i
            if i!=0:
                judge=False
        if pr!=0:
            return len(nums)
        else:
            if judge:
                return 0
            else:
                return len(nums)-1
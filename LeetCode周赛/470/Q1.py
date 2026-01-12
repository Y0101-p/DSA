from typing import List
class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)):
            if i%2==0:
                res+=nums[i]
            else:
                res-=nums[i]
        return res
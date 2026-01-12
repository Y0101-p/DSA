from typing import List
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        l=set()
        maxi=-float('inf')
        for i in nums:
            if i>0:
                l.add(i)
            maxi=max(maxi,i)
        if maxi<=0:
            return maxi 
        return sum(l)
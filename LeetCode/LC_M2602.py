from itertools import accumulate
from typing import List
import bisect

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prev_sum = list(accumulate(nums, initial=0))
        res=[]
        n=len(nums)
        for i in queries:
            left_index = bisect.bisect_left(nums, i)
            left_sum = prev_sum[left_index]
            right_sum = prev_sum[-1]-prev_sum[left_index]
            res.append(left_index*i-left_sum+right_sum-(n-left_index)*i)
        return res
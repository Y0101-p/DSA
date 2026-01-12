from typing import List
from collections import defaultdict
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(num):
            res=str(num)[::-1]
            return int(res)

        dic = {}
        ans = 10**6
        for i in range(len(nums)):
            if nums[i] in dic:
                ans = min(ans, i-dic.get(nums[i]))
            rev = reverse(nums[i])
            dic[rev]=i

        if ans==10**6:
            return -1
        else:
            return ans


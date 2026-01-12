from typing import List
class Solution:
    def splitArray(self, nums: List[int]) -> int:
        def find_end():
            for i in range(1,len(nums)):
                if nums[i-1]>=nums[i]:
                    return i-1
            return len(nums)-1
        def check_right(mid):
            for i in range(mid+1,len(nums)):
                if nums[i]>=nums[i-1]:
                    if i==mid+1 and nums[i]==nums[i-1]:
                        continue
                    return True
            return False
        mid=find_end()
        if check_right(mid):
            return -1
        else:
            res=abs(sum(nums[:mid+1])-sum(nums[mid+1:]))
            if nums[mid]>nums[mid+1]:
                res=min(res,abs(sum(nums[:mid])-sum(nums[mid:])))
            return res
sol=Solution()
print(sol.splitArray([2,2]))
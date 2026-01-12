from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        def check(nums,target,mid):
            s=sum(nums[:mid])
            if s>=target:
                return nums[:mid]
            
            for i in range(len(nums)-mid):
                s=s+nums[mid+i]-nums[i]
                if s>=target:
                    return nums[i+1:mid+i+1]
            return False
        left=0
        right=len(nums)
        if sum(nums)<target:
            return 0
        while right>=left:
            mid=(left+right)//2
            if check(nums,target,mid):
                right=mid-1
            else:
                left=mid+1
        return left
print(Solution.minSubArrayLen(None,7,[2,3,1,2,4,3]))
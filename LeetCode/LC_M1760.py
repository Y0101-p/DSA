from typing import List
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def check(nums,mid):
            t=0
            for i in nums:
                t +=(i-1)//mid
                if t>maxOperations:
                    return True
            return False
        
        left=1
        right=max(nums)+1
        ans=-1
        while right>left:
            mid=(left+right)//2
            if check(nums,mid):
                left =mid+1
            else:
                right=mid
                ans=mid
        return ans

if __name__ == '__main__':
    solution = Solution()
    res = solution.minimumSize(nums = [10,10,10,10,10,10], maxOperations = 5)
    print(res)
from typing import List
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans=0
        lenth=len(nums)
        blist=[i for i in range(lenth)]
        for i in range(lenth):
            for j in range(i+1,lenth):
                for k in range(max(j+1,blist[j]),lenth):
                    if nums[i]+nums[j]>nums[k]:
                        blist[j]=k
                        if k==lenth-1:
                            ans +=blist[j]-j
                    else:
                        ans +=blist[j]-j
                        break
        return ans  
solution=Solution()
nums=[24,3,82,22,35,84,19]
print(solution.triangleNumber(nums))
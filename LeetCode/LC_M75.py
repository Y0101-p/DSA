from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n=len(nums)
        red=0
        blue=n-1
        white=0
        kong=0
        while white<=blue:
            if nums[white]==0 and white>red:
                kong=nums[white]
                nums[white]=nums[red]
                nums[red]=kong
                red +=1
                continue
            elif nums[white]==2:
                kong=nums[white]
                nums[white]=nums[blue]
                nums[blue]=kong
                blue -=1
                continue
            white +=1
        return nums

if __name__=='__main__':
    nums=[2,0,0]
    solution=Solution()
    res=solution.sortColors(nums)
    print(res)
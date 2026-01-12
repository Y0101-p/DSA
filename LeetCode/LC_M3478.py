from typing import List
import heapq
class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n=len(nums1)
        sorted_num1=[]
        for i in range(n):
            sorted_num1.append((nums1[i],i))
        sorted_num1.sort(key=lambda x:x[0])
        l=[]
        t=0
        res=[0]*n
        s=0
        adds=0
        for i in range(1,n):
            if len(l)<k:
                heapq.heappush(l,nums2[sorted_num1[i-1][1]])
            else:
                s -=heapq.heappushpop(l,nums2[sorted_num1[i-1][1]])
            s +=nums2[sorted_num1[i-1][1]]
            if sorted_num1[i][0]>sorted_num1[t][0]:
                t=i
                adds=s    
            res[sorted_num1[i][1]]=adds
        return res



if __name__=='__main__':
    solution=Solution()
    res=solution.findMaxSum([25,15,1,28,3,13,29,26,1,2,28,5,2,14,19,2,4], 
                            [25,21,3,23,26,6,30,22,27,21,24,27,15,17,15,16,25], 
                            k = 9)
    print(res)
from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def check(mid,cit):
            if cit[-mid]>=mid:
                return True
            else:
                return False
        citations.sort()
        left=0
        right=len(citations)
        while right>=left:
            mid=(left+right)//2
            if check(mid,citations):
                left =mid +1
            else:
                right =mid -1
        return right
if __name__=='__main__':
    solution=Solution()
    res=solution.hIndex(citations =[1,3,1])
    print(res)
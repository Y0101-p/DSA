from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def finlow(alist:List[int],xiangzuo:bool)-> List[int]:
            stack=[]
            lenth=len(alist)
            res=[0]*lenth
            if xiangzuo:
                for i in range(lenth):
                    if len(stack)==0:
                        stack.append(i)
                        res[i]=i
                    else:
                        while alist[stack[-1]]>=alist[i]:
                            stack.pop()
                            if len(stack)==0:
                                res[i]=0
                                break
                        if len(stack)!=0:
                            res[i]=stack[-1]+1
                        stack.append(i)
            else:
                for i in range(-1,-lenth-1,-1):
                    if len(stack)==0:
                        stack.append(i)
                        res[i]=i+lenth
                    else:
                        while alist[stack[-1]]>=alist[i]:
                            stack.pop()
                            if len(stack)==0:
                                res[i]=-1+lenth
                                break
                        if len(stack)!=0:
                            res[i]=stack[-1]-1+lenth
                        stack.append(i)
            return res
        
        left=finlow(heights,True)
        right=finlow(heights,False)
        maxi=0
        for i in range(len(heights)):
            maxi=max(maxi,heights[i]*(right[i]-left[i]+1))
        return maxi
if __name__=='__main__':
    solution=Solution()
    heights = [2,1,5,6,2,3]
    res=solution.largestRectangleArea(heights)
    print(res)
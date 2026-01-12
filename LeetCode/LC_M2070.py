from typing import List
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        def check(items,a):
            left=0
            right=len(items)-1
            if a>=items[-1][0]:
                return right
            if a<items[0][0]:
                return -1
            while right>=left:
                mid=(left+right)//2
                if items[mid][0]>a:
                    right=mid-1
                else:
                    left=mid+1
            return right
        sorted_quries=[]
        items.sort(key=lambda x:x[0])
        for i in range(len(queries)):
            sorted_quries.append((queries[i],i))
        sorted_quries.sort(key=lambda x:x[0])
        res=[0]*len(queries)
        peak=[0]
        maxi=0
        for i in sorted_quries:
            t=check(items,i[0])
            peak.append(t)
            for j in range(max(peak[-2],0),t+1):
                maxi=max(maxi,items[j][1])
            res[i[1]]=maxi
        return res

if __name__=='__main__':
    solution=Solution()
    res=solution.maximumBeauty([[193,732],[781,962],[864,954],[749,627],[136,746],[478,548],[640,908],[210,799],[567,715],[914,388],[487,853],[533,554],[247,919],[958,150],[193,523],[176,656],[395,469],[763,821],[542,946],[701,676]]
                               ,[885,1445,1580,1309,205,1788,1214,1404,572,1170,989,265,153,151,1479,1180,875,276,1584])
    print(res)
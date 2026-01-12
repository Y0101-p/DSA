class Solution:
    def beautySum(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            l=[0]*26
            for j in range(i,len(s)):
                l[ord(s[j])-97] +=1
                mini=114514
                for k in l:
                    if k<mini and k!=0:
                        mini=k    
                res +=max(l)-mini
        return res
print(Solution.beautySum(None,'aabcb'))
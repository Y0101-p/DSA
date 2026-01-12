class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        r=r-l
        pr_a=[i for i in range(r+1)]
        pr_b=[0 for i in range(r+1)]
        cnt=0
        while cnt<n-3:
            if cnt%2==0:
                for i in range(-2,-r-2,-1):
                    pr_b[i]=pr_b[i+1]+pr_a[i+1]
            else:
                for i in range(1,r+1):
                    pr_a[i]=pr_b[i-1]+pr_a[i-1]
            cnt+=1
        res=0
        if cnt%2==0:
            for i in range(r+1):
                res=(res+pr_a[i]*i)%(10**9 + 7)
            res=(res*2)%(10**9 + 7)
        else:
            for i in range(r+1):
                res=(res+pr_b[i]*(r-i))%(10**9 + 7)
            res=(res*2)%(10**9 + 7)
        return res

sol=Solution()
print(sol.zigZagArrays(3,1,3))
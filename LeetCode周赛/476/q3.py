class Solution:
    def countDistinct(self, n: int) -> int:
        def count_feishou(s):
            if s=='':
                return 1
            if s[0]=='0':
                return 0
            else:
                return ((int(s[0])-1)*count_feishou('9'*len(s[1:]))+
                        count_feishou(s[1:]))
        def count(n):
            if n<10:
                return n
            res=0
            if len(str(n))>1:
                res+=count_feishou(str(n)[1:])+(int(str(n)[0])-1)*9**(len(str(n))-1)
            length=len(str(n))-1
            for i in range(length):
                res+=9**(length-i)
            return res
        return count(n)

sol=Solution()
print(sol.countDistinct(1000))
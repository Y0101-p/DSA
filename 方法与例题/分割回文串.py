from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def check(astr):
            if astr[::-1]==astr:
                return True
            else:
                return False
        def dfs(s,res,path,deep,size):
            if s=='':
                res.append(path[:])
                return
            for i in range(1,size+1):
                a=s[:i]
                if check(a):
                    path.append(a)
                    dfs(s[i:],res,path,deep,len(s[i:]))
                    path.pop()

            
        dfs(s,res,[],0,len(s))
        return res

if __name__ == '__main__':
    s = 'aab'
    solution = Solution()
    res = solution.partition(s)
    print(res)
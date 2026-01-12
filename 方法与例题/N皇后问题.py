from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        

        def dfs(deep,n,res,huanghou):
                if deep==n:
                    res.append(huanghou[:])
                    return
                for i in range(n):
                    if i in huanghou:
                        continue
                    judge=0
                    for j in range(deep):
                        dx=deep-j
                        dy=i-huanghou[j]
                        if dx+dy==0 or dx==dy:
                            judge=1
                            break
                    if judge==1:
                        continue
                    huanghou.append(i)
                    dfs(deep+1,n,res,huanghou)
                    huanghou.pop()
        res=[]
        huanghou=[]    
        dfs(0,n,res,huanghou)
        ans=[]
        for i in range(len(res)):
            qipan=[]
            for j in range(n):
                row=['.']*n
                row[res[i][j]]='Q'
                astr=''.join(row)
                qipan.append(astr)
            ans.append(qipan)


        return ans






if __name__ == '__main__':
    n = 7
    solution = Solution()
    res = solution.solveNQueens(n)
    print(res)
from typing import List
class Solution_written_by_YH:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board,word,hax,deep,size,res,h,l,x,y):
            if deep==size:
                res.append(True)
                return
            if deep==0:
                for i in range(h):
                    for j in range(l):
                        if board[i][j]==word[0]:
                            hax[i][j]=False
                            dfs(board,word,hax,1,size,res,h,l,j,i)
                            hax[i][j]=True
            else:
                if y-1>=0:
                    if board[y-1][x]==word[deep] and hax[y-1][x]:
                        hax[y-1][x]=False
                        dfs(board,word,hax,deep+1,size,res,h,l,x,y-1)
                        hax[y-1][x]=True
                if y+1<h:
                    if board[y+1][x]==word[deep] and hax[y+1][x]:
                        hax[y+1][x]=False
                        dfs(board,word,hax,deep+1,size,res,h,l,x,y+1)
                        hax[y+1][x]=True
                if x-1>=0:
                    if board[y][x-1]==word[deep] and hax[y][x-1]:
                        hax[y][x-1]=False
                        dfs(board,word,hax,deep+1,size,res,h,l,x-1,y)
                        hax[y][x-1]=True                        
                if x+1<l:
                    if board[y][x+1]==word[deep] and hax[y][x+1]:
                        hax[y][x+1]=False
                        dfs(board,word,hax,deep+1,size,res,h,l,x+1,y)
                        hax[y][x+1]=True        


        size=len(word)
        res=[]
        l=len(board[0])
        h=len(board)
        hax=[[True] * l for _ in range(h)]
        for i in range(h):
            for j in range(l):
                if board[i][j] not in word:
                    hax[i][j]=False
        dfs(board,word,hax,0,size,res,h,l,0,0)
        if len(res)>0:
            return True
        else:
            return False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(i: int, j: int, k: int) -> bool:
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            
            visited.add((i, j))
            result = False
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if (newi, newj) not in visited:
                        if check(newi, newj, k + 1):
                            result = True
                            break
            
            visited.remove((i, j))
            return result

        h, w = len(board), len(board[0])
        visited = set()
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True
        
        return False


if __name__ == '__main__':
    board=[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
    word='ABCCEDG'
    solution = Solution()
    res = solution.exist(board,word)
    print(res)
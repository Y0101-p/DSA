from collections import deque
class TreeNode:
    def __init__(self,x,left=None,right=None):
        self.val = x
        self.left = left
        self.right = right
        self.parent = None


n=int(input())
l=[TreeNode(i) for i in range(1,n+1)]
for i in range(n):
    t=list(map(int,input().split()))
    if t[0]!=-1:
        l[i].left=l[t[0]-1]
        l[t[0]-1].parent=l[i]
    if t[1]!=-1:
        l[i].right=l[t[1]-1]
        l[t[1]-1].parent=l[i]
for j in l:
    if not j.parent:
        root=j

blist=deque([(root,1)])
while blist:
    t=blist.popleft()
    if t[0].left:
        blist.append((t[0].left,t[1]+1))
    if t[0].right:
        blist.append((t[0].right,t[1]+1))
    lenth=t[1]
print(lenth)
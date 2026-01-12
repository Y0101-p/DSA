import sys

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def read_num(index):
    res=''
    while data[index].isnumeric():
        res+=data[index]
        index+=1
    return int(res),index

def preorder(node,s,num):
    if node.left:
        if preorder(node.left,s+node.val,num):
            return True
    if node.right:
        if preorder(node.right,s+node.val,num):
            return True
    if not(node.left) and not(node.right):
        if s+node.val == num:
            return True
        else:
            return False
    return False
data=sys.stdin.read().strip().split()
data=''.join(data)
data=list(data)
index=0
stack=[]

while index < len(data):
    if not stack:
        if data[index]=='(':
            stack.append(data[index])
            index+=1
        elif data[index].isnumeric():
            num,index=read_num(index)
        elif data[index]=='-':
            index+=1
            num,index=read_num(index)
            num=-num
    else:
        if data[index]=='(':
            stack.append(data[index])
            index+=1
        elif data[index].isnumeric():
            pr_val,index=read_num(index)
            pr=TreeNode(pr_val)
            stack.append([0,pr])
        elif data[index]=='-':
            index+=1
            pr_val,index=read_num(index)
            pr_val=-pr_val
            pr=TreeNode(pr_val)
            stack.append([0,pr])
        elif data[index]==')':
            t=stack.pop()
            pr=None
            while t!='(':
                pr=t[1]
                t=stack.pop()
            if stack:
                parent=stack[-1]
                if parent[0]==0:
                    parent[1].left=pr
                    parent[0]+=1
                elif parent[0]==1:
                    parent[1].right=pr
            else:
                root=pr
                if root and preorder(root,0,num):
                    print('yes')
                else:
                    print('no')
            index+=1

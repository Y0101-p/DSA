class TreeNode:
    def __init__(self,val:str,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    def preorder(self,res:str):
        res+=self.val
        if self.left:
            res=self.left.preorder(res)
        if self.right:
            res=self.right.preorder(res)
        return res

def insert_tree(root:TreeNode,new_node:str):
    if new_node>root.val:
        if root.right:
            insert_tree(root.right,new_node)
        else:
            root.right = TreeNode(new_node)
    else:
        if root.left:
            insert_tree(root.left,new_node)
        else:
            root.left = TreeNode(new_node)
alist=[]
while True:
    l=input()
    if l=='*'or l=='$':
        root=TreeNode(alist[-1])
        alist.pop()
        while alist:
            t=alist.pop()
            for i in t:
                insert_tree(root,i)
        print(root.preorder(''))
        alist.clear()
        if l=='$':
            break
    else:
        alist.append(l)
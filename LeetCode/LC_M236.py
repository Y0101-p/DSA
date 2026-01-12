class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def check(pr:'TreeNode',target:'TreeNode'):
            if pr:
                if (pr.val,target.val) in check_dic:
                    return check_dic[(pr.val,target.val)]
                if pr.val==target.val:
                    check_dic[(pr.val,target.val)]=True
                    return True
                else:
                    if check(pr.left,target) or check(pr.right,target):
                        check_dic[(pr.val,target.val)]=True
                        return True
                    else:
                        check_dic[(pr.val,target.val)]=False
                        return False
            else:
                return False

        def dfs(pr:'TreeNode',p:'TreeNode',q:'TreeNode'):
            if pr:
                dfs(pr.left,p,q)
                if check(pr.left,p) and check(pr.left,q):
                    res.append(pr.left)
                dfs(pr.right,p,q)
                if check(pr.right,p) and check(pr.right,q):
                    res.append(pr.right)
                if check(pr,p) and check(pr,q):
                    res.append(pr)
            else:
                return
        check_dic={}
        res=[]
        check(root,p)
        check(root,q)
        dfs(root,p,q)
        if res:
            return res[0]
        else:
            return root
root=TreeNode(3)
root.left=TreeNode(5)
p=root.left
root.right=TreeNode(1)
root.left.left=TreeNode(6)
root.left.right=TreeNode(2)
root.left.right.left=TreeNode(7)
root.left.right.right=TreeNode(4)
q=root.left.right.right
root.right.left=TreeNode(0)
root.right.right=TreeNode(8)
print(Solution().lowestCommonAncestor(root,p,q).val)
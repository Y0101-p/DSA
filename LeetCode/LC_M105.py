from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(pr,left_index,right_index,k):
            if pr and k<len(preorder):
                root_inorder_index=dic[pr.val]
                if root_inorder_index>left_index:
                    pr.left=TreeNode(preorder[k])
                    k=build(pr.left,left_index,root_inorder_index-1,k+1)
                if root_inorder_index<right_index:
                    pr.right=TreeNode(preorder[k])
                    k=build(pr.right,root_inorder_index+1,right_index,k+1)
            return k
        dic={}
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        root=TreeNode(preorder[0])
        build=build(root,0,len(inorder)-1,1)
        return root


print(Solution().buildTree(preorder=[3,9,20,15,7], inorder=[9,3,15,20,7]))
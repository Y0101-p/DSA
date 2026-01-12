from typing import Optional
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def postorder_dp(root):
            if root:
                left_max_root,left_max_no_root=postorder_dp(root.left)
                right_max_root,right_max_no_root=postorder_dp(root.right)
                return left_max_no_root+right_max_no_root+root.val,max(left_max_root,left_max_no_root)+max(right_max_root,right_max_no_root)
            else:
                return 0,0
        return max(postorder_dp(root))
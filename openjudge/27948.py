from collections import deque
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        res.append(root.val)

n = int(input())
data = input()
queue = deque()
for i in data:
    if i=='1':
        queue.append(TreeNode('I'))
    else:
        queue.append(TreeNode('B'))
while len(queue)>1:
    left = queue.popleft()
    right = queue.popleft()
    if left.val==right.val:
        new_pr = TreeNode(left.val, left, right)
    else:
        new_pr = TreeNode('F', left, right)
    queue.append(new_pr)
root = queue.popleft()
res = []
postorder(root)
print(''.join(res))
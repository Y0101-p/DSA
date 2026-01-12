from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.child = []

def postorder(root):
    if root:
        for child in root.child:
            postorder(child)
        res.append(root.val)


n = int(input())
tree_list = []
res = []
for i in range(n):
    data = list(input().split())
    root = TreeNode(data[0])
    root_cnt = int(data[1])
    queue = deque()
    queue.append([root, root_cnt])
    for index in range(2,len(data),2):
        pr = TreeNode(data[index])
        cnt = int(data[index+1])
        while queue[0][1] == 0:
            queue.popleft()
        parent = queue[0][0]
        parent.child.append(pr)
        queue[0][1] -= 1

        queue.append([pr,cnt])

    postorder(root)
print(*res)
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def preorder(root):
    if root:
        pre_res.append(root.val)
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        in_res.append(root.val)
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        post_res.append(root.val)
n=int(input())
for i in range(n):
    pre_res = []
    in_res = []
    post_res = []
    stack_dic={}
    while True:
        data = input()
        if data == '0':
            break
        if data[0] == '-':
            deep=len(data)-1
            val=data[-1]
            if val=='*':
                t=stack_dic[deep-1].pop()
                stack_dic[deep-1].append((t[0],t[1]+1))
                continue
            pr=TreeNode(val)
            t=stack_dic[deep-1].pop()
            parent=t[0]
            if t[1]==0:
                parent.left=pr
                stack_dic[deep-1].append((parent,t[1]+1))
            else:
                parent.right=pr
            stack_dic.setdefault(deep,[]).append((pr,0))
        else:
            root = TreeNode(data)
            stack_dic[0] = [(root,0)]
    preorder(root)
    inorder(root)
    postorder(root)
    print(''.join(pre_res))
    print(''.join(post_res))
    print(''.join(in_res))
    print()
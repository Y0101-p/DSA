"""
class Trie:
    def __init__(self):
        self.num_list=[None]*10
        self.end=False
t=int(input())
for i in range(t):
    n=int(input())
    head=Trie()
    judge=True
    for j in range(n):
        l=input()
        if not judge:
            continue
        pr=head
        for k in range(len(l)-1):
            if pr.end:
                judge = False
                break
            num=int(l[k])
            if pr.num_list[num]:
                pr=pr.num_list[num]
            else:
                pr.num_list[num]=Trie()
                pr=pr.num_list[num]
        num=int(l[-1])
        if pr.num_list[num] or not judge or pr.end:
            judge=False
        else:
            pr.num_list[num] = Trie()
            pr.num_list[num].end=True
    if judge:
        print('YES')
    else:
        print('NO')
"""

def add(nums,pr):
    for k in range(len(nums)):
        if nums[k] not in pr:
            pr[nums[k]] = {}
            pr=pr[nums[k]]
        else:
            pr=pr[nums[k]]
            if pr=={}:
                return False
    if pr!={}:
        return False
    else:
        return True
t=int(input())
for i in range(t):
    n=int(input())
    root={}
    judge=True
    for j in range(n):
        nums=input()
        if judge:
            if not add(nums,root):
                print('NO')
                judge=False
    if judge:
        print('YES')
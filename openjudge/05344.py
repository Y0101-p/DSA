class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


n, k = map(int, input().split())
root = ListNode(1)
pr = root
for i in range(2,n+1):
    pr.next = ListNode(i)
    pr = pr.next
pr.next = root
pr = root
res = []
while pr.next != pr:
    for i in range(k-1):
        prev = pr
        pr = pr.next
    res.append(pr.val)
    prev.next = pr.next
    pr = pr.next

print(*res)
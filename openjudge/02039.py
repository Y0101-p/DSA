n = int(input())
data = input().strip()
alist = [[] for i in range(n)]
cnt = 0
a_cnt = 0
for i in data:
    if a_cnt % 2 == 0:
        alist[cnt].append(i)
    else:
        alist[-cnt-1].append(i)
    cnt = (cnt + 1) % n
    if cnt == 0:
        a_cnt += 1

res = ''
for i in alist:
    res += ''.join(i)
print(res)
from collections import defaultdict
import heapq

n, k = map(int, input().split())
data = list(map(int, input().split()))
k_set = set(map(int, input().split()))
k_min = 0
other_max = 0

time_dic = defaultdict(list)
for i in range(0, 2*n, 2):
    t, c = data[i], data[i+1]
    time_dic[t].append(c)
time_dic = dict(sorted(time_dic.items()))

if k == 314159:
    res = 0
    for i in time_dic:
        res = max(res, i)
    print(res)
    exit()

ticket_list = [0]*(314159+1)
res = 0
prev = 0
heap = []
for i in k_set:
    heap.append((0, i))

for i in time_dic:
    k_min = heap[0][0]
    if k_min > other_max:
        res += i - prev
    prev = i

    for j in time_dic[i]:
        ticket_list[j] = ticket_list[j] + 1
        if j in k_set:
            heapq.heappush(heap, (ticket_list[j], j))

        else:
            other_max = max(other_max, ticket_list[j])

    while heap[0][0] < ticket_list[heap[0][1]]:
        heapq.heappop(heap)

print(res)

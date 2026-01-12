import heapq
from collections import defaultdict
stack = []
lazy_dic = defaultdict(int)
heap = []
while True:
    try:
        data = input()
        if data[0:4]=='push':
            weight = int(data[5:])
            stack.append(weight)
            heapq.heappush(heap, weight)
        elif data[0:3]=='pop':
            if stack:
                weight = stack.pop()
                lazy_dic[weight] += 1
        else:
            if stack:
                t = heapq.heappop(heap)
                while t in lazy_dic:
                    lazy_dic[t] -= 1
                    if lazy_dic[t] == 0:
                        lazy_dic.pop(t)
                    t = heapq.heappop(heap)
                print(t)
                heapq.heappush(heap, t)
    except EOFError:
        break
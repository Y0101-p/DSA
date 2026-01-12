from collections import defaultdict
import math
import heapq

def count_distance(a,b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    if a in neighbor_dic[b] or b in neighbor_dic[a]:
        return  math.sqrt(dx * dx + dy * dy)/4
    else:
        return  math.sqrt(dx * dx + dy * dy)

start_x,start_y,end_x,end_y=map(int,input().split())
start = (start_x,start_y)
end = (end_x,end_y)
neighbor_dic = defaultdict(set)
translate_dic = {start: 0, end: 1}
cnt = 2
while True:
    try:
        line = list(map(int,input().split()))
        left_x, left_y = line[0], line[1]
        left = (left_x,left_y)
        if left not in translate_dic:
            translate_dic[left] = cnt
            cnt += 1
        for i in range(2,len(line),2):
            x = line[i]
            y = line[i+1]
            if x==-1 and y==-1:
                break
            pr = (x,y)
            neighbor_dic[pr].add(left)
            neighbor_dic[left].add(pr)
            left = pr
            if pr not in translate_dic:
                translate_dic[pr] = cnt
                cnt += 1
    except EOFError:
        break

distance = [float('inf')]*cnt
distance[0] = 0
visited = [False]*cnt
heap = [(0,start)]
while heap and not visited[1]:
    dis, pr = heapq.heappop(heap)
    if visited[(translate_dic[pr])]:
        continue
    else:
        visited[translate_dic[pr]] = True
        for i in translate_dic:
            if visited[(translate_dic[i])]:
                continue
            else:
                index = translate_dic[i]
                new_dis = dis + count_distance(pr, i)
                if new_dis < distance[index]:
                    distance[index] = new_dis
                    heapq.heappush(heap, (new_dis, i))

res = distance[1]/(1000/6)
print(round(res))
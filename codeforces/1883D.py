import heapq
def weihuduicing():
    while left_heap:
        t=heapq.heappop(left_heap)
        if t in left_dic:
            left_dic[t] -=1
            if left_dic[t]==0:
                left_dic.pop(t)
        else:
            heapq.heappush(left_heap,t)
            break
    while right_heap:
        t=heapq.heappop(right_heap)
        if t in right_dic:
            right_dic[t] -=1
            if right_dic[t]==0:
                right_dic.pop(t)
        else:
            heapq.heappush(right_heap,t)
            break    
left_heap=[]
right_heap=[]
q=int(input())
left_dic={}
right_dic={}
for i in range(q):
    shuru=input().split()
    if shuru[0]=='+':
        heapq.heappush(left_heap,-int(shuru[1]))
        heapq.heappush(right_heap,int(shuru[2]))
    else:
        left_dic.setdefault(-int(shuru[1]),0)
        right_dic.setdefault(int(shuru[2]),0)
        left_dic[-int(shuru[1])] +=1
        right_dic[int(shuru[2])] +=1
        weihuduicing()   
    if left_heap and right_heap and -left_heap[0]>right_heap[0]:
        print('YES')
    else:
        print('NO')
#这个方法有明显的漏洞
#pylint:skip-file
from collections import deque
import heapq
class medium:
    def __init__(self):
        self.numlist=deque([])
        self.min_heap=[(float('inf'),float('inf'))]
        self.max_heap=[(float('inf'),float('inf'))]
        self.lenth=0
        self.query=0
        self.delline=-1
    def __add__(self,x):
        i=self.lenth+self.delline+1
        self.numlist.append((x,i))
        if self.lenth%2==0:
            while True:
                t=heapq.heappop(self.max_heap)
                if t[1]>self.delline:
                    heapq.heappush(self.max_heap,t)
                    break
            if self.numlist[-1][0]<=self.max_heap[0][0]:
                heapq.heappush(self.min_heap,(-self.numlist[-1][0],self.numlist[-1][1]))
                while True:##可能是多余的代码
                    t=heapq.heappop(self.min_heap)
                    if t[1] >self.delline:
                        heapq.heappush(self.min_heap,t)
                        break
            else:
                heapq.heappush(self.max_heap,self.numlist[-1])
                t=heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap,(-t[0],t[1]))
                while True:##可能是多余的代码
                    t=heapq.heappop(self.max_heap)
                    if t[1]>self.delline:
                        heapq.heappush(self.max_heap,t)
                        break               
            self.query=-self.min_heap[0][0]
        else:
            while True:
                t=heapq.heappop(self.min_heap)
                if t[1]>self.delline:
                    heapq.heappush(self.min_heap,t)
                    break
            if self.numlist[-1][0]>-self.min_heap[0][0]:
                heapq.heappush(self.max_heap,self.numlist[-1])
                while True:##可能是多余的代码
                    t=heapq.heappop(self.max_heap)
                    if t[1]>self.delline:
                        heapq.heappush(self.max_heap,t)
                        break
            else:
                heapq.heappush(self.min_heap,(-self.numlist[-1][0],self.numlist[-1][1]))
                t=heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap,(-t[0],t[1]))
                while True:##可能是多余的代码
                    t=heapq.heappop(self.min_heap)
                    if t[1] >self.delline:
                        heapq.heappush(self.min_heap,t)
                        break   
            self.query=(-self.min_heap[0][0]+self.max_heap[0][0])/2                       
        self.lenth +=1
    def __del__(self):
        x=self.numlist.popleft()
        self.delline +=1
        if self.lenth%2==0:
            if x[0]<self.max_heap[0][0]:
                t=heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap,(-t[0],t[1]))
            self.query=-self.min_heap[0][0]
            while True:
                t=heapq.heappop(self.max_heap)
                if t[1]>self.delline:
                    heapq.heappush(self.max_heap,t)
                    break
        else:
            if x[0]>=self.max_heap[0][0]:##此处有显著漏洞，不应该讨论索引，而是应该用词典记录次数
                t=heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap,(-t[0],t[1]))               
            while True:
                t=heapq.heappop(self.min_heap)
                if t[1]>self.delline:
                    heapq.heappush(self.min_heap,t)
                    self.query=(-t[0]+self.max_heap[0][0])/2
                    break
        self.lenth -=1


    def __query__(self):
        if self.lenth==0:
            print(0)
        elif round(self.query)==self.query:
            print(int(self.query))
            res.append(int(self.query))
        else:
            print(self.query)
            res.append(self.query)
    def __check__(self,a):
        if a[0]=='a':
            medium.__add__(self,float(a[4:]))
        elif a[0]=='d':
            medium.__del__(self)
        else:
            medium.__query__(self)
        return

if __name__=='__main__':
    n=int(input())
    solution=medium()
    res=[]
    for i in range(n):
        a=input()
        solution.__check__(a)
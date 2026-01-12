class Heap:
    def __init__(self):
        self.heap=[]
    def push(self,val):
        self.heap.append(val)
        self.up_balance(len(self.heap)-1)
    def pop(self):
        self.heap[0],self.heap[-1]=self.heap[-1],self.heap[0]
        t=self.heap.pop()
        self.down_balance(0)
        return t
    def up_balance(self,pr):
        if pr==0:
            return
        parent_index=(pr-1)//2
        if self.heap[parent_index]>self.heap[pr]:
            self.heap[parent_index],self.heap[pr]=self.heap[pr],self.heap[parent_index]
            self.up_balance(parent_index)
        else:
            return
    def down_balance(self,pr):
        left=pr*2+1
        right=pr*2+2
        if left>len(self.heap)-1:
            return
        elif left==len(self.heap)-1:
            if self.heap[left]<self.heap[pr]:
                self.heap[left],self.heap[pr]=self.heap[pr],self.heap[left]
            return
        else:
            if self.heap[pr]<min(self.heap[right],self.heap[left]):
                return
            else:
                if self.heap[left]<self.heap[right]:
                    self.heap[left],self.heap[pr]=self.heap[pr],self.heap[left]
                    self.down_balance(left)
                else:
                    self.heap[right],self.heap[pr]=self.heap[pr],self.heap[right]
                    self.down_balance(right)
n=int(input().strip())
heap=Heap()
for i in range(n):
    l=tuple(map(int,input().strip().split()))
    if l[0]==1:
        heap.push(l[1])
    elif l[0]==2:
        print(heap.pop())
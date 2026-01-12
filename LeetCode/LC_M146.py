class node:
    def __init__(self,key):
        self.next=None
        self.last=None
        self.key=key
class LRUCache:
    def __init__(self, capacity: int):
        self.cache={}
        self.capacity=capacity
        self.head=None
        self.end=None
    def get(self, key: int) -> int:
        if key in self.cache:
            if len(self.cache)==1:
                return self.cache[key][0]
            pr=self.cache[key][1]
            if pr.next==None:
                return self.cache[key][0]
            if pr.key!=self.head.key:
                pr.last.next=pr.next
            else:
                self.head=pr.next
            if pr.key!=self.end.key:
                pr.next.last=pr.last
            pr.next=None
            pr.last=self.end
            self.end.next=pr
            self.end=pr
            return self.cache[key][0]       
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if len(self.cache)==self.capacity and key not in self.cache:
            self.cache.pop(self.head.key)
            self.head=self.head.next
        if key in self.cache:
            if len(self.cache)==1:
                self.cache[key]=(value,node(key))
                return
            pr=self.cache[key][1]
            if pr.next==None:
                self.cache[key]=(value,pr)
                return
            if pr.key!=self.head.key:
                pr.last.next=pr.next
            else:
                self.head=pr.next
            if pr.key!=self.end.key:
                pr.next.last=pr.last
            pr.next=None
            pr.last=self.end
            self.end.next=pr
            self.end=pr
            self.cache[key]=(value,pr)          
        else:
            self.cache[key]=(value,node(key))
            if self.head==None:
                self.head=self.cache[key][1]
                self.end=self.cache[key][1]
            else:
                self.end.next=self.cache[key][1]
                self.cache[key][1].last=self.end
                self.end=self.end.next

lRUCache=LRUCache(2)
lRUCache.put(2, 6)
lRUCache.get(1)    
lRUCache.put(1, 5) 
lRUCache.put(1,2)
lRUCache.get(1) 
lRUCache.get(2)
lRUCache.get(4)
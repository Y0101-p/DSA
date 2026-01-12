class Allocator:
    def __init__(self, n: int):
        self.neicun=['_']*n
        self.lenth=n
    def allocate(self, size: int, mID: int) -> int:
        t=0
        for i in range(self.lenth):
            if self.neicun[i]=='_':
                t +=1
            else:
                t=0
            if t==size:
                zancun=self.neicun[:i-size+1]+[mID]*size
                if i<self.lenth-1:
                    zancun +=self.neicun[i+1:]
                self.neicun=zancun
                return i-size+1
        return -1
    def freeMemory(self, mID: int) -> int:
        t=0
        for i in range(self.lenth):
            if self.neicun[i]==mID:
                t +=1
                self.neicun[i]='_'
        return t
if __name__=='__main__':
    All=Allocator(10)
    print(All.allocate(1,1))
    print(All.allocate(9,3))
    print(All.allocate(9,9))

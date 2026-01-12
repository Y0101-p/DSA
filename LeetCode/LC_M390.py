class Solution:
    def lastRemaining(self, n: int) -> int:
        t=0
        stack=[]
        while n>1:
            if t%2==0:
                if n%2==0:
                    n=n//2
                    stack.append(0)
                else:
                    n=(n-1)//2
                    stack.append(0)
            else:
                if n%2==0:
                    n=n//2
                    stack.append(1)
                else:
                    n=(n-1)//2
                    stack.append(0)
            t +=1
        t -=1
        while stack:
            if stack.pop():
                n=n*2-1
                t-=1
            else:
                if t%2==0:
                    n *=2
                    t -=1
                else:
                    n =n*2
                    t -=1
        return n
print(Solution.lastRemaining(None,6))
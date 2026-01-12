class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        res=[]
        lenth=len(str(n))
        for i in range(lenth):
            next_n=n%(10**(len(str(n))-1))
            res.append(n-next_n)
            n=next_n
        return res



class Fraction:
    def __init__(self,fenzi,fenmu):
        self.fenmu=fenmu
        self.fenzi=fenzi
    def jiafa(self,x):
        z=Fraction((x.fenzi)*(self.fenmu)+(x.fenmu)*(self.fenzi),x.fenmu*self.fenmu)
        return Fraction.yuefen(z)
    def yuefen(self):
        maxi=1
        for i in range(2,max(self.fenzi,self.fenmu)+1):
            if self.fenzi%i==0 and self.fenmu%i==0:
                maxi=max(maxi,i)
        return Fraction(self.fenzi//maxi,self.fenmu//maxi)
    def print1(self):
        print(f'{self.fenzi}/{self.fenmu}')
if __name__ == '__main__':
    alist=list(map(int,input().split()))
    a=Fraction(alist[0],alist[1])
    b=Fraction(alist[2],alist[3])
    c=Fraction.jiafa(a,b)
    Fraction.print1(c)
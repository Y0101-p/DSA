def hannuota(n,begin,end,mid):
    if n==1:
        res.append(f'1:{begin}->{end}')
        return
    else:
        hannuota(n-1,begin,mid,end)
        res.append(f'{n}:{begin}->{end}')
        hannuota(n-1,mid,end,begin)
        return        
import sys
n,a,b,c=input().split()
res=[]
n=int(n)
hannuota(n,a,c,b)
sys.stdout.write('\n'.join(res)+'\n')
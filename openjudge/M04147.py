def yidong(n,begin,mid,end):
    if n==1:
        res.append(f'1:{begin}->{end}')
    elif n==2:
        res.append(f'1:{begin}->{mid}')
        res.append(f'2:{begin}->{end}')
        res.append(f'1:{mid}->{end}')
    else:
        yidong(n-1,begin,end,mid)
        res.append(f'{n}:{begin}->{end}')
        yidong(n-1,mid,begin,end)
n,a,b,c=input().split()
res=[]
yidong(int(n),a,b,c)
for i in res:
    print(i)
    
n=int(input())
dic={}
for i in range(n):
    num,m,d=map(str,input().split())
    m=int(m)
    d=int(d)
    dic.setdefault((m,d),[]).append(num)
sort_dic=dict(sorted(dic.items(),key=lambda x:(x[0][0],x[0][1])))
for i,nums in sort_dic.items():
    if len(nums)<=1:
        continue
    out=' '.join(nums)
    m=i[0]
    d=i[1]
    print(f"{m} {d} {out}")
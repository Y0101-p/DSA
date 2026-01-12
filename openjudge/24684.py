#11：35
dic={}
alist=list(map(int,input().split()))
for i in alist:
    dic.setdefault(i,0)
    dic[i] +=1
sorted_dic=dict(sorted(dic.items(),key=lambda x:(-x[1],x[0])))
peak=float('inf')
res=[]
for i in sorted_dic:
    if peak==float('inf'):
        peak=sorted_dic[i]
        res.append(i)
    else:
        if peak==sorted_dic[i]:
            res.append(i)
        else:
            break
ans=' '.join(map(str,res))
print(ans)
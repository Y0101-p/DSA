#10：35
n=int(input())
dic1={}
dic2={}
for i in range(n):
    alist=input().split()
    for j in alist[1:]:
        if i+1 not in dic2.setdefault(j,set()):
            dic2[j].add(i+1)
            dic1.setdefault(j,[]).append(i+1)

m=int(input())
for i in range(m):
    s=input()
    if s in dic1:
        print(' '.join(map(str,dic1[s])))
    else:
        print('NOT FOUND')
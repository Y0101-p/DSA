row=int(input())
astr=input()
l=len(astr)
alist=[]
i=0
t=0
while i+row<=l:
    if t%2==0:
        alist.append(list(astr[i:i+row]))
    else:
        alist.append(list(astr[i+row-1:i-1:-1]))
    t +=1
    i +=row
res=''
for j in range(row):
    for i in range(len(alist)):
        res +=alist[i][j]
print(res)
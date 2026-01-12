n=int(input())
zimudic={'A':'2','B':'2','C':'2','D':'3','E':'3','F':'3'
         ,'G':'4','H':'4','I':'4','J':'5','K':'5','L':'5'
         ,'M':'6','N':'6','O':'6','P':'7','R':'7','S':'7'
         ,'T':'8','U':'8','V':'8','W':'9','X':'9','Y':'9'}
numdic={}
for i in range(n):
    s=input()
    s.upper()
    num=''
    for j in s:
        if j.isnumeric():
            num +=j
        elif j in zimudic:
            num +=zimudic[j]
        if len(num)==3:
            num +='-'
    numdic.setdefault(num,0)
    numdic[num] +=1
res=[]
for i,j in numdic.items():
    if j>=2:
        res.append((i,j))
res.sort()
if len(res)==0:
    print('No duplicates.')
else:
    for i in res:
        print(i[0],i[1])
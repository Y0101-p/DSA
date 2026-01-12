d=int(input())
n=int(input())
alist=[]
for i in range(n):
    alist.append(tuple(map(int,input().split())))
max_bomb_num=0
max_num=0
for i in range(1025):
    for j in range(1025):
        bomb_num=0
        mini=(i-d,j-d)
        maxi=(i+d,j+d)
        for k in alist:
            if mini[0]<=k[0]<=maxi[0] and mini[1]<=k[1]<=maxi[1]:
                bomb_num +=k[2]
        if bomb_num>max_bomb_num:
            max_bomb_num=bomb_num
            max_num=1
        elif bomb_num==max_bomb_num:
            max_num +=1
print(max_num,max_bomb_num)
while True:
    alist=list(map(int,input().split()))
    if sum(alist)==0:
        break
    res=alist[5]
    res+=alist[4]
    alist[0]-=alist[4]*11
    res+=alist[3]
    left=alist[3]*5
    if left>alist[1]:
        alist[0] -=(left-alist[1])*4
        alist[1]=0
    else:
        alist[1]-=left
    res+=alist[2]//4
    left=4-alist[2]%4
    res+=1
    if left==4:
        res-=1
    elif left==1:
        if alist[1]>0:
            alist[1]-=1
            alist[0]-=5
        else:
            alist[1]=0
            alist[0]-=9
    elif left==2:
        if alist[1]>3:
            alist[1] -=3
            alist[0] -=6
        else:
            kong=(3-alist[1])*4+6
            alist[0]-=kong
            alist[1]=0
    elif left==3:
        if alist[1]>5:
            alist[1] -=5
            alist[0] -=7
        else:
            kong=(5-alist[1])*4+7
            alist[0]-=kong
            alist[1]=0
    if alist[1]>0:
        res +=alist[1]//9
        left=alist[1]%9
        if left!=0:
            res+=1
            left =9-left
            alist[0] -=left*4
    if alist[0]>0:
        res +=alist[0]//36
        if alist[0]%36!=0:
            res +=1
    print(res)
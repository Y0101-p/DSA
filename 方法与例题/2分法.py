def fen2_search(a,list):
    low=0
    high=len(list)-1
    while low<=high:
        mid=(low+high)//2
        g=list[mid]
        if(g==a):
            return mid
        if(g>a):
            high=mid-1
        else:
            low=mid+1
    return None 



def fen2_insert(l1,a):
    x=0
    y=len(l1-1)
    mid=(x+y)//2
    if l1[y]<=a:
        return y+1
    if l1[x]>=a:
        return 0
    while x<y-1:
        if l1[mid]==a:
            return mid
        if l1[mid]>a:
            y=mid
        else:
            x=mid
        mid=(x+y)//2
    return y
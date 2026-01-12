def merge_count(alist):
    left=0
    right=len(alist)-1
    mid=(left+right)//2
    if right<=0:
        return 0,alist
    elif right==1:
        if alist[0]>alist[1]:
            return 1,[alist[1],alist[0]]
        else:
            return 0,alist
    else:
        left_count,left_arr=merge_count(alist[:mid])
        right_count,right_arr=merge_count(alist[mid:])
        i,j=0,0
        arr=[]
        count=0
        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i]<=right_arr[j]:
                arr.append(left_arr[i])
                i +=1
            else:
                arr.append(right_arr[j])
                j +=1
                count +=len(left_arr)-i
        arr.extend(left_arr[i:])
        arr.extend(right_arr[j:])
        return left_count+count+right_count,arr
while True:
    t=int(input())
    if t==0:
        break
    alist=[]
    for i in range(t):
        alist.append(int(input()))
    print(merge_count(alist)[0])

    
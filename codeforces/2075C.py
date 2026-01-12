import sys
import bisect

data = sys.stdin.read().splitlines()
index = 0
t=int(data[index])
index+=1
for i in range(t):
    n,m = map(int, data[index].split())
    index+=1
    a_list=list(map(int, data[index].split()))
    index+=1
    a_list.sort()
    res=0
    left_num=1
    right_num=n-1
    left=0
    right=len(a_list)-1
    while left_num<=right_num:
        left=bisect.bisect_left(a_list,left_num,left,right)
        right=bisect.bisect_left(a_list,right_num,left,right)
        if a_list[right]<right_num :
            right_num=a_list[right]
            left_num=n-a_list[right]
            continue

        if left_num==right_num:
            left = bisect.bisect_left(a_list, left_num, left, right)
            right = bisect.bisect_left(a_list, right_num, left, right)
            res +=  (m - left - 1) * (m - right)
            break
        else:
            res += 2 * (m - left - 1) * (m - right)
            left_num += 1
            right_num -= 1
    print(res)
n=int(input())
for i in range(1,n+1):
    left,right=map(int,input().split())
    cnt_left,cnt_right=0,0
    while left!=right:
        if left>right:
            if right!=1:
                cnt_left+=left//right
                left%=right
            else:
                cnt_left+=left-1
                left=1
        else:
            if left!=1:
                cnt_right+=right//left
                right%=left
            else:
                cnt_right+=right-1
                right=1
    print(f'Scenario #{i}:')
    print(cnt_left,cnt_right)
    print()
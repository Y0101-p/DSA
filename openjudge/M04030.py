target=input().strip().lower()
str_list=input()
cnt=0
first_index=-1
pr_begin=0
pr_end=0
while pr_end<len(str_list):
    if str_list[pr_begin]==' ':
        pr_begin+=1
        pr_end+=1
    else:
        while pr_end<len(str_list) and  str_list[pr_end]!=' ' :
            pr_end+=1
        word=str_list[pr_begin:pr_end].lower()
        if word==target:
            cnt+=1
            if first_index==-1:
                first_index=pr_begin
        pr_begin=pr_end
if cnt>0:
    print(cnt,first_index)
else:
    print(-1)
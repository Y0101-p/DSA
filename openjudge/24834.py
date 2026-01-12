def check(s,p):
    lenth_s=len(s)
    lenth_p=len(p)
    pr_s=0
    pr_p=0
    while pr_s<lenth_s and pr_p<lenth_p:
        if p[pr_p].isalpha():
            if p[pr_p]!=s[pr_s]:
                return False
            pr_p+=1
            pr_s+=1
        else:
            if p[pr_p]=='?':
                pr_p +=1
                pr_s +=1
            else:
                for k in range(lenth_s-pr_s+1):
                    if check(s[pr_s+k:],p[pr_p+1:]):
                        return True
                return False
            
    if pr_p==lenth_p and pr_s==lenth_s:
        return True
    elif pr_p<lenth_p:
        t=p[pr_p:]
        for i in t:
            if i!='*':
                return False
        return True
    else:
        return False


n=int(input())
for i in range(n):
    s=input()
    p=input()
    if check(s,p):
        print('yes')
    else:
        print('no')
    
while True:
    try:
        s=input()
        stack=[]
        ans=[' ']*len(s)
        right=[]
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            if s[i]==')':
                if len(stack)>0:
                    stack.pop()
                else:
                    right.append(i)
        for i in stack:
            ans[i]='$'
        for j in right:
            ans[j]='?'
        res=''.join(ans)
        print(s)
        print(res)
    except EOFError:
        break
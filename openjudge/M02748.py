def dfs(s,deep,path,size):
    if deep == size:
        print(''.join(path))
        return
    for i in s:
        if i not in path:
            path.append(i)
            dfs(s,deep+1,path,size)
            path.pop()
s=input()
dfs(s,0,[],len(s))

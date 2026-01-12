while True:
    try:
        n=input().strip()
        if n[0]=='@' or n[0]=='.' or n[-1]=='@' or n[-1]=='.':
            print('NO')
            continue
        if n.count('@')!=1:
            print('NO')
            continue
        t=n.find('@')
        s=n.find('.',t+1)
        if n[t+1]=='.' or n[t-1]=='.':
            print('NO')
            continue
        print("YES")
    except EOFError:
        break

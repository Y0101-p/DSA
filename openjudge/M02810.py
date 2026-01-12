n=int(input())
for i in range(6,n+1):
    for b in range(2,i):
        c=b
        d=i-1
        while c<=d:
            if b**3+c**3+d**3==i**3:
                print(f'Cube = {i}, Triple = ({b},{c},{d})')
                c+=1
            elif b**3+c**3+d**3>i**3:
                d-=1
            else:
                c+=1
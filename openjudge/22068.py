from collections import Counter
def check(x,y):
    stack=[]
    res=[]
    t=0
    for i in range(len(x)):
        stack.append(x[i])
        while len(stack)>0 and stack[-1]==y[t]:
            t +=1
            stack.pop()
    if t==len(y):
        return True
    else:
        return False

x=input()
x_dic=Counter(x)
while True:
    try:
        y=input()
        y_dic=Counter(y)
        if x_dic!=y_dic:
            print('NO')
            continue
        if check(x,y):
            print('YES')
        else:
            print('NO')
    except EOFError:
        break
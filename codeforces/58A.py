##10:47
s=input()
dic='hello'
t=0
for i in s:
    if i==dic[t]:
        t +=1
    if t==5:
        print('YES')
        exit()
print('NO')

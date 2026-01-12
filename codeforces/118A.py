#10:56
s=input()
s=s.lower()
res=''
yuanyin=['a','o','y','e','u','i']
for i in s:
    if i in yuanyin:
        continue
    else:
        res +=f'.{i}'
print(res)
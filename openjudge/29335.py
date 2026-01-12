path = input().split('/')
stack = []
for i in path:
    if i == '..':
        if stack:
            stack.pop()
    elif i == '.' or i == '':
        continue
    else:
        stack.append(i)
res = '/'.join(stack)
print('/'+res)

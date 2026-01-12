

l=list(input().split())
num_stack=[['','']]
fuhao_stack=[]
check=0
for i in range(len(l)):
    if l[i]=="+" or l[i]=="-" or l[i]=='*' or l[i]=='/':
        fuhao_stack.append(l[i])
        num_stack.append(['',''])
    else:
        if num_stack[-1][0]=='':
            num_stack[-1][0]=float(l[i])
        else:
            num_stack[-1][1]=float(l[i])
            while len(num_stack)>1:
                if num_stack[-2][0]=='':
                    num_stack[-2][0]=eval(str(num_stack[-1][0])+fuhao_stack[-1]+str(num_stack[-1][1]))                    
                    num_stack.pop()
                    fuhao_stack.pop()                
                    break
                num_stack[-2][1]=eval(str(num_stack[-1][0])+fuhao_stack[-1]+str(num_stack[-1][1]))
                num_stack.pop()
                fuhao_stack.pop()

print("%f\n"% float(num_stack[0][0]))
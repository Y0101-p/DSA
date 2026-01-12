from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack=[]
        for i in tokens:
            if i=="*" or i=='/' or i=='+' or i=='-':
                num_stack[-2]=str(int((eval(num_stack[-2]+i+num_stack[-1]))))
                num_stack.pop()   
            else:
                num_stack.append(i)
       
        return num_stack[0]

if __name__=="__main__":
    solution=Solution()
    res=solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
    print(res)
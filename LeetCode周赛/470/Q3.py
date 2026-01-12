class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        stack=[]
        res=''
        for i in range(len(s)):
            if s[i]=='(':
                if stack and stack[-1][0]=='(':
                    t=stack.pop()
                    stack.append(('(',t[1]+1))
                else:
                    stack.append(('(',1))
            else:
                if stack and stack[-1][0]==')':
                    t=stack.pop()
                    stack.append((')',t[1]+1))
                else:
                    stack.append((')',1))
                if stack[-1][1]== k:
                    if len(stack) >= 2 and stack[-2][0] == '(' and stack[-2][1] >= k:
                        stack.pop()
                        a = stack.pop()
                        if a[1] > k:
                            stack.append(('(', a[1] - k))
        for j in stack:
            res+=j[0]*j[1]
        return res
sol=Solution()
print(sol.removeSubstring(s = "(()(", k = 1))
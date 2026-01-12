class Solution:
    def resultingString(self, s: str) -> str:
        res_stack = []
        stack = []
        for char in s[::-1]:
            stack.append(char)
        while stack:
            t = stack.pop()
            if not res_stack:
                res_stack.append(t)
            else:
                r = res_stack[-1]
                if abs( ord(t) - ord(r) ) == 1 or (r == 'z' and t == 'a') or (r == 'a' and t == 'z'):
                    res_stack.pop()
                else:
                    res_stack.append(t)

        return ''.join(res_stack)

s = 'zadb'
sol = Solution()
print(sol.resultingString(s))
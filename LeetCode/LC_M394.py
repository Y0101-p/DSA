class Solution:
    def decodeString(self, s: str) -> str:
        numstack=[1]
        strstack=['']
        num=''
        for i in range(len(s)):
            if s[i].isnumeric():
                num +=s[i]
            elif s[i]=='[':
                numstack.append(int(num))
                strstack.append('')
                num=''
            elif s[i]==']':
                strstack[-2] +=strstack[-1]*numstack[-1]
                numstack.pop()
                strstack.pop()
            else:
                strstack[-1] +=s[i]
        return strstack[-1]

if __name__ == '__main__':
    solution = Solution()
    mat = "3[a]2[bc]"
    res = solution.decodeString(mat)
    print(res)
s = input()
res = 0
for i in range(len(s)):
    res += (ord(s[-i-1])-64) * 26**i

print(res)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def Manacher_d1(n, s):
            d1 = [0] * n
            l, r = 0, -1
            for i in range(0, n):
                if i > r:
                    k = 1
                else:
                    k = min(d1[l + r - i], r - i + 1)

                while 0 <= i - k and i + k < n and s[i - k] == s[i + k]:
                    k += 1
                d1[i] = k
                k -= 1

                if i + k > r:
                    l = i - k
                    r = i + k

            return d1


        alist=['*']
        for i in s:
            alist +=[i,'*']
        d1 = Manacher_d1(len(alist), alist)
        maxi =1
        max_index = 0
        for i in range(len(alist)):
            if d1[i] > maxi:
                maxi = d1[i]
                max_index = i
        res = ''
        for i in alist[max_index-d1[max_index]+1:max_index+d1[max_index]]:
            if i != '*':
                res += i
        return res

if __name__=='__main__':
    solution=Solution()
    res=solution.longestPalindrome('cbbd')
    print(res)
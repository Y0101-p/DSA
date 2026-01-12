from collections import Counter
class Solution:
    def maxDistinct(self, s: str) -> int:
        counter = Counter(s)
        return len(counter)

sol = Solution()
s = 'aaaa'
print(sol.maxDistinct(s))
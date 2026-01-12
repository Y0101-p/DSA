from collections import Counter


class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        dic = Counter(s)

        return abs(dic.get('a',0) - dic.get('b',0))
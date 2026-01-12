class KmpByYH:
    def build_next(self,s):
        next = [0]
        curr_predix_len = 0
        i = 1
        while i < len(s):
            if s[i] == s[curr_predix_len]:
                curr_predix_len += 1
                next.append(curr_predix_len)
                i += 1
            else:
                if curr_predix_len == 0:
                    next.append(curr_predix_len)
                    i += 1
                else:
                    curr_predix_len = next[curr_predix_len - 1]

        return next

    def search(self,s, target):
        next = self.build_next(s)

        i = 0
        j = 0
        while i < len(target):
            if s[j] == target[i]:
                j += 1
                i += 1

            else:
                if j > 0:
                    j = next[j - 1]
                else:
                    i += 1

            if j == len(s):
                return i - j


class KmpByYhf:
    """
    compute_lps 函数用于计算模式字符串的LPS表。LPS表是一个数组，
    其中的每个元素表示模式字符串中当前位置之前的子串的最长前缀后缀的长度。
    该函数使用了两个指针 length 和 i，从模式字符串的第二个字符开始遍历。
    """

    def compute_lps(self,pattern):
        """
        计算pattern字符串的最长前缀后缀（Longest Proper Prefix which is also Suffix）表
        :param pattern: 模式字符串
        :return: lps表
        """

        m = len(pattern)
        lps = [0] * m  # 初始化lps数组
        length = 0  # 当前最长前后缀长度
        for i in range(1, m):  # 注意i从1开始，lps[0]永远是0
            while length > 0 and pattern[i] != pattern[length]:
                length = lps[length - 1]  # 回退到上一个有效前后缀长度
            if pattern[i] == pattern[length]:
                length += 1
            lps[i] = length

        return lps

    def kmp_search(self, text, pattern):
        n = len(text)
        m = len(pattern)
        if m == 0:
            return 0
        lps = self.compute_lps(pattern)
        matches = []

        # 在 text 中查找 pattern
        j = 0  # 模式串指针
        for i in range(n):  # 主串指针
            while j > 0 and text[i] != pattern[j]:
                j = lps[j - 1]  # 模式串回退
            if text[i] == pattern[j]:
                j += 1
            if j == m:
                matches.append(i - j + 1)  # 匹配成功
                j = lps[j - 1]  # 查找下一个匹配

        return matches


text = "ABABABABCABABABABCABABABABC"
pattern = "ABABCABAB"
sol = KmpByYH()
index = sol.search(pattern, text)
print("pos matched：", index)
# pos matched： [4, 13]

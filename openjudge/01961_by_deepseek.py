import sys


def build_next(s):
    """构建KMP的next数组"""
    n = len(s)
    next_arr = [0] * n
    j = 0  # 前缀指针

    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = next_arr[j - 1]

        if s[i] == s[j]:
            j += 1

        next_arr[i] = j

    return next_arr


def find_periods_kmp(n, s):
    """使用KMP算法找出所有前缀的循环节"""
    next_arr = build_next(s)
    result = []

    for i in range(1, n):  # i从1开始，因为前缀长度至少为2才可能有循环节
        length = i + 1  # 前缀长度
        cycle_len = length - next_arr[i]

        # 判断是否有循环节：长度能被循环节长度整除，且循环节长度小于字符串长度
        if length % cycle_len == 0 and cycle_len < length:
            k = length // cycle_len  # 循环次数
            if k > 1:  # 题目要求K>1
                result.append((length, k))

    return result


def main():
    case_cnt = 1
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            continue

        n = int(line)
        if n == 0:
            break

        s = sys.stdin.readline().strip()

        print(f'Test case #{case_cnt}')
        periods = find_periods_kmp(n, s)

        for length, k in periods:
            print(f'{length} {k}')

        print()  # 空行
        case_cnt += 1


if __name__ == "__main__":
    main()
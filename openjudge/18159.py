from bisect import bisect_left

def oula(n):
    hax = [True] * (n + 1)
    prime = []
    ans = []
    for i in range(2, n + 1):
        if hax[i]:
            prime.append(i)
            if str(i)[-1] == '1':
                ans.append(i)
            hax[i] = False
        for j in prime:
            t = i * j
            if t > n:
                break
            hax[t] = False
            if i % j == 0:
                break
    return ans


t = int(input())
ans = oula(10001)
for i in range(t):
    n = int(input())
    index = bisect_left(ans, n)
    print(f'Case{i+1}:')
    if index >= len(ans):
        if ans[-1] < n:
            print(*ans)
        else:
            print(*ans[:-1])
    elif n <= 11:
        print('NULL')
    else:
        print(*ans[:index])

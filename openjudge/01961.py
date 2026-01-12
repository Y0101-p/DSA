import sys
sys.setrecursionlimit(1000000)


def judge(index, n):
    cnt = 2
    while cnt*(index+1) <= n:
        new_index = cnt*(index+1)-1
        if s[new_index - index:new_index + 1] == s[:index + 1]:
            predix[new_index] = min(predix[index], predix[new_index])
            visited[new_index] = True
        else:
            visited[index] = True
            return

        cnt += 1
    visited[index] = True
    return


case_cnt = 1
while True:
    n = int(input())
    if n == 0:
        exit()
    s = input()

    predix = [i+1 for i in range(n)]

    visited = [False]*n

    for i in range(n//+1):
        if not visited[i]:
            judge(i, n)

    print(f'Test case #{case_cnt}')
    case_cnt += 1
    for i in range(n):
        if i+1 != predix[i]:
            print(i+1, (i+1)//predix[i])

    print()
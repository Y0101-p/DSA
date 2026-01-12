from collections import deque
from collections import defaultdict


def check():
    queue = deque([])
    degree_list = in_degree.copy()
    cache = [[]]
    for node in degree_list:
        if degree_list[node] == 0:
            queue.append((node, 0))

    index = 0
    while queue:
        pr, cnt = queue.popleft()
        if cnt > index:
            cache.append([])
            index += 1
        cache[-1].append(pr)
        for node in graph[pr]:
            degree_list[node] -= 1
            if degree_list[node] == 0:
                queue.append((node, cnt+1))

    judge = False
    for node in degree_list:
        if degree_list[node] != 0:
            judge = True
    if judge:
        return False, None
    else:
        return True, cache


while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    data = []
    for i in range(m):
        data.append(input())
    graph = defaultdict(set)
    str_list = {}
    in_degree = defaultdict(int)
    finished = False
    finish_time = 0
    success = True
    res = []
    for i in range(m):
        left, right = data[i][0], data[i][2]
        graph[left].add(right)
        in_degree[right] += 1
        if left not in in_degree:
            in_degree[left] = 0
        no_loop, res = check()
        if no_loop:
            if len(res) == n:
                for j in range(n):
                    str_list[res[j][0]] = j
                finished = True
                finish_time = i + 1
                break
        else:
            finish_time = i + 1
            success = False
            break

    if success:
        if finished:
            ans = ''
            for j in res:
                ans += j[0]
            print(f'Sorted sequence determined after {finish_time} relations: {ans}.')
        else:
            print('Sorted sequence cannot be determined.')
    else:
        print(f'Inconsistency found after {finish_time} relations.')

from collections import deque


def dfs(begin, end, w, h):
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([begin])
    visited = [[float('inf')]*(w+2) for _ in range(h+2)]
    visited[begin[0]][begin[1]] = 0
    while queue:
        x, y = queue.popleft()
        step = visited[x][y]+1
        for dx, dy in direction:
            k = 0
            while True:
                k += 1
                nx = x + k*dx
                ny = y + k*dy
                if 0 <= nx <= h+1 and 0 <= ny <= w+1:
                    if step < visited[nx][ny]:
                        visited[nx][ny] = step
                        queue.append((nx, ny))
                        if matrix[nx][ny] == 1:
                            queue.pop()
                            break
                    elif matrix[nx][ny] == 1:
                        break
                else:
                    break
    if visited[end[0]][end[1]] == float('inf'):
        return -1
    else:
        return visited[end[0]][end[1]]


cnt = 1
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    matrix = [[0]*(w+2) for _ in range(h+2)]
    data = [input() for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if data[i][j] == 'X':
                matrix[i+1][j+1] = 1
    print(f'Board #{cnt}:')
    cnt += 1
    pair_cnt = 1
    while True:
        y1, x1, y2, x2 = map(int, input().split())
        if x1 == 0 and y1 == 0:
            break
        steps = dfs((x1, y1), (x2, y2), w, h)
        if steps == -1:
            print(f'Pair {pair_cnt}: impossible.')
        else:
            print(f'Pair {pair_cnt}: {steps} segments.')
        pair_cnt += 1
    print()
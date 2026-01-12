from collections import deque


def main():
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(input()))
    visited = [[0] * m for _ in range(n)]
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    search_queue = [deque() for _ in range(4)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '.':
                continue
            else:
                if visited[i][j] == 0:

                    queue = deque([(i, j)])
                    cnt += 1
                    visited[i][j] = cnt
                    while queue:
                        x, y = queue.popleft()

                        for dx, dy in direction:
                            new_x = x + dx
                            new_y = y + dy
                            if 0 <= new_x < n and 0 <= new_y < m and matrix[new_x][new_y] == 'X' and visited[new_x][new_y] == 0:
                                visited[new_x][new_y] = cnt
                                queue.append((new_x, new_y))

                        for dx, dy in direction:
                            new_x = x + dx
                            new_y = y + dy
                            if 0 <= new_x < n and 0 <= new_y < m and matrix[new_x][new_y] == '.':
                                search_queue[cnt].append((x, y, 0))
                                break

    dis_matrix = [[[float('inf')] * m for _ in range(n)] for j in range(3) ]

    def dis_count(dis_matrix, search, m, n, cnt):

        while search:
            x, y, dis = search.popleft()
            for dx, dy in direction:
                if 0<= x+dx <n and 0<= y+dy <m:

                    if visited[x+dx][y+dy] == 0 and dis_matrix[x+dx][y+dy] > dis+1:
                        dis_matrix[x+dx][y+dy] = dis+1
                        search.append((x+dx, y+dy, dis+1))
                    elif visited[x+dx][y+dy] != cnt and visited[x+dx][y+dy] != 0 and dis_matrix[x+dx][y+dy] > dis:
                        dis_matrix[x+dx][y+dy] = dis
                        search.append((x+dx, y+dy, dis))


    for i in range(1,4):
        dis_count(dis_matrix[i-1], search_queue[i], m, n, i)


    ans = float('inf')

    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0:
                s = dis_matrix[0][i][j] + dis_matrix[1][i][j] + dis_matrix[2][i][j] - 2
                if s < ans:
                    ans = s
            elif visited[i][j] == 1:
                s = dis_matrix[1][i][j] + dis_matrix[2][i][j]
                if s < ans:
                    ans = s
            elif visited[i][j] == 2:
                s = dis_matrix[0][i][j] + dis_matrix[2][i][j]
                if s < ans:
                    ans = s
            elif visited[i][j] == 3:
                s = dis_matrix[0][i][j] + dis_matrix[1][i][j]
                if s < ans:
                    ans = s

    print(ans)


if __name__ == '__main__':
    main()

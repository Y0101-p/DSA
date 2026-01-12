import heapq


def astar(maze, start, end, R, C):
    # 方向：上、右、下、左
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # 开放列表：(f值, g值, 行, 列)
    open_list = []
    heapq.heappush(open_list, (0, 0, start[0], start[1]))

    # 记录每个节点的g值（到达该节点的实际代价）
    g_values = {start: 0}

    # 记录每个节点的父节点，用于回溯路径
    parents = {}

    while open_list:
        # 取出f值最小的节点
        current_f, current_g, row, col = heapq.heappop(open_list)
        current_pos = (row, col)

        # 如果到达终点
        if current_pos == end:
            # 回溯路径计算步数,此题可以直接返回g值
            steps = 0
            while current_pos in parents:
                current_pos = parents[current_pos]
                steps += 1
            return steps

        # 检查四个方向的邻居
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            new_pos = (new_row, new_col)

            # 检查边界和墙壁
            if (0 <= new_row < R and 0 <= new_col < C and
                    maze[new_row][new_col] != '#'):

                # 计算新的g值
                new_g = current_g + 1

                # 如果新路径更好，更新
                if new_pos not in g_values or new_g < g_values[new_pos]:
                    g_values[new_pos] = new_g
                    # 计算启发函数（曼哈顿距离）
                    h_value = abs(new_row - end[0]) + abs(new_col - end[1])
                    f_value = new_g + h_value

                    heapq.heappush(open_list, (f_value, new_g, new_row, new_col))
                    parents[new_pos] = current_pos

    # 无法到达终点
    return -1


def astar_with_closed_list(maze, start, end, R, C):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    open_list = []
    heapq.heappush(open_list, (0, 0, start[0], start[1]))

    g_values = {start: 0}
    closed_set = set()  # 严格的关闭列表

    while open_list:
        current_f, current_g, row, col = heapq.heappop(open_list)
        current_pos = (row, col)

        # 如果节点已在关闭列表中，跳过
        if current_pos in closed_set:
            continue

        closed_set.add(current_pos)  # 标记为已关闭

        if current_pos == end:
            return current_g

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            new_pos = (new_row, new_col)

            # 检查是否在关闭列表中
            if new_pos in closed_set:
                continue  # 跳过已关闭的节点

            if (0 <= new_row < R and 0 <= new_col < C and
                    maze[new_row][new_col] != '#'):

                new_g = current_g + 1

                # 在这种情况下，new_g < g_values[new_pos] 不会出现
                # 因为关闭列表中的节点不会被重新考虑
                if new_pos not in g_values:  # 只需检查是否首次访问
                    g_values[new_pos] = new_g
                    h_value = abs(new_row - end[0]) + abs(new_col - end[1])
                    f_value = new_g + h_value
                    heapq.heappush(open_list, (f_value, new_g, new_row, new_col))

    return -1





def solve_maze():
    T = int(input().strip())
    for _ in range(T):
        R, C = map(int, input().split())
        maze = []
        start = end = None

        # 读取迷宫并定位起点和终点
        for i in range(R):
            row = list(input().strip())
            maze.append(row)
            for j in range(C):
                if row[j] == 'S':
                    start = (i, j)
                elif row[j] == 'E':
                    end = (i, j)

        result = astar_with_closed_list(maze, start, end, R, C)
        if result == -1:
            print("oop!")
        else:
            print(result)





# 运行示例
if __name__ == "__main__":
    solve_maze()
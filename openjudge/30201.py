

def main():
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    size = 1 << n

    dp = [[float("inf")] * n for _ in range(size)]
    dp[1][0] = 0

    for i in range(1, size, 2):
        for j in range(n):

            if dp[i][j] == float("inf"):
                continue

            cur_cost = dp[i][j]

            for k in range(n):
                if (1 << k) & i:
                    continue
                new_cost = cur_cost + graph[j][k]
                new_mask = (1 << k) | i

                if dp[new_mask][k] > new_cost:
                    dp[new_mask][k] = new_cost

    res = float("inf")
    for i in range(n):
        cost = dp[-1][i] + graph[i][0]
        if res > cost:
            res = cost
    print(res)


if __name__ == "__main__":
    main()

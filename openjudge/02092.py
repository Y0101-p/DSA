from collections import defaultdict
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    score = defaultdict(int)

    for i in range(n):
        data = list(map(int, input().split()))
        for j in data:
            score[j] += 1

    res_list = []
    for i in score:
        res_list.append((score[i], i))
    res_list.sort(key=lambda x:(-x[0], x[1]))
    base = res_list[1][0]
    number_two = []
    for score, i in res_list[1:]:
        if score == base:
            number_two.append(i)
        else:
            break
    print(*number_two)
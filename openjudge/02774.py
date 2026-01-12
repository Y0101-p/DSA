def check(mid, k):
    s = 0
    for i in length_list:
        s += (i//mid)

    if s >= k:
        return True
    else:
        return False

n, k = map(int, input().split())
length_list = [int(input()) for _ in range(n)]
if sum(length_list) < k:
    print(0)
else:
    left = 1
    right = max(length_list)
    while left <= right:
        mid = (left + right) // 2
        if check(mid, k):
            left = mid + 1
        else:
            right = mid - 1
    print(right)
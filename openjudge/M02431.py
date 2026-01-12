import heapq

def main():
    n = int(input())
    data_list = [(0, 0)]
    for i in range(n):
        dist, fuel = map(int, input().split())
        data_list.append((dist, fuel))
    data_list.sort()
    curr_l, curr_p = map(int, input().split())
    while data_list[-1][0] > curr_l:
        data_list.pop()

    curr_min = curr_l - curr_p
    cnt = 0
    heap = []
    while curr_min > 0 and data_list:
        dist, fuel = data_list.pop()
        while curr_min > dist:
            if not heap:
                return -1
            delta = heapq.heappop(heap)
            curr_min += delta
            cnt += 1
        heapq.heappush(heap, -fuel)

    return cnt


if __name__ == "__main__":
    print(main())

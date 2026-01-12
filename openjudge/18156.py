def main():
    t = int(input())
    num_list = list(map(int, input().split()))
    num_list.sort()
    left = 0
    right = len(num_list) - 1
    res = num_list[left]+num_list[right]
    while left < right:
        if num_list[left] + num_list[right] > t:
            while num_list[left] + num_list[right-1] > t and left+1 < right:
                right -= 1
            if abs(res-t) > num_list[left] + num_list[right] - t:
                res = num_list[left] + num_list[right]
            right -= 1
        elif num_list[left] + num_list[right] < t:
            while num_list[left+1] + num_list[right] < t and left+1 < right:
                left += 1
            if abs(res-t) >= abs(t - num_list[left] - num_list[right]):
                res = num_list[left] + num_list[right]
            left += 1
        else:
            print(t)
            return
    print(res)
    return


if __name__ == '__main__':
    main()
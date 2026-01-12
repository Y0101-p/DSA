def Manacher_d1(n, s):
    d1 = [0] * n
    l, r = 0, -1
    for i in range(0, n):
        if i > r:
            k = 1
        else:
            k = min(d1[l + r - i], r - i + 1)

        while 0 <= i - k and i + k < n and s[i - k] == s[i + k]:
            k += 1
        d1[i] = k
        k -= 1

        if i + k > r:
            l = i - k
            r = i + k

    return d1


def Manacher_d2(n, s):
    d2 = [0] * n
    l, r = 0, -1
    for i in range(0, n):
        k = 0 if i > r else min(d2[l + r - i + 1], r - i + 1)
        while 0 <= i - k - 1 and i + k < n and s[i - k - 1] == s[i + k]:
            k += 1
        d2[i] = k
        k -= 1
        if i + k > r:
            l = i - k - 1
            r = i + k
    return d2

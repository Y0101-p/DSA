

def main():
    d = int(input())
    n = int(input())
    c = {}
    for i in range(n):
        x, y, z = map(int, input().split())
        for p in range(max(0, x - d), min(1024, x + d) + 1):
            for q in range(max(0, y - d), min(1024, y + d) + 1):
                c[(p, q)] = c.setdefault((p, q), 0) + z
    a = list(c.values())
    s = max(a)
    print(a.count(s), s)


if __name__ == '__main__':
    main()

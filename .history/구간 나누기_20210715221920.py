n, k = map(int, input().split())


def solve():
    for i in range(k):
        if (n-i) % k == 0:
            return i


ans = solve()
print(ans+(n-ans)//k)

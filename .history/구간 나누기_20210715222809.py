n, k = map(int, input().split())


def solve():
    i = 0
    while n > 0:
        n = n/k
        i += 1
    return i-1


print(solve()+n)

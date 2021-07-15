n, k = map(int, input().split())
Sum = 1


def solve():
    i = 0
    while Sum < n:
        Sum = Sum*k
        i += 1
    return i+n % Sum


print(solve())

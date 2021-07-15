n, k = map(int, input().split())
Sum = 1


def solve():
    global Sum
    i = 0
    while Sum*k < n:
        Sum = Sum*k
        i += 1
    return i+n % Sum


print(solve())

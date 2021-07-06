

def dfs(x, y):
    if x == n-1 and y == n-1:
        return 1
    if dp[x][y] == -1:
        dp[x][y] == 0
        if x+Map[x][y] < n:
            dp[x][y] += dfs(x+Map[x][y], y)
        if y+Map[x][y] < n:
            dp[x][y] += dfs(x, y+Map[x][y])
    return dp[x][y]


if __name__ == "__main__":
    n = int(input())
    Map = [list(map(int, input().split()))for _ in range(n)]
    dp = [[-1]*n for _ in range(n)]
    print(dfs(0, 0))

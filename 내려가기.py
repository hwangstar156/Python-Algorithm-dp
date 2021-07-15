n = int(input())
str = []
for i in range(n):
    str.append(int(input()))
dp = [-1]*201


def lis(start):
    if dp[start+1] != -1:
        return dp[start+1]
    dp[start+1] = 1
    for i in range(start+1, n):
        if start == -1 or str[start] < str[i]:
            dp[start+1] = max(dp[start+1], lis(i)+1)
    return dp[start+1]


print(n-lis(-1)+1)

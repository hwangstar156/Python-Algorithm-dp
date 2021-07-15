n = int(input())
str = []
for i in range(n):
    str.append(int(input()))
dp = [-1]*201


def lis(start):
    if dp[start] != -1:
        return dp[start]
    dp[start] = 1
    for i in range(start+1, n):
        if start == -1 or str[start] < str[i]:
            dp[start] = max(dp[start], lis(i)+1)
    return dp[start]


lis(0)
print(n-max(dp))

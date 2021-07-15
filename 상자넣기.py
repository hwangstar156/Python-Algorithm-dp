n = int(input())
arr = list(map(int, input().split()))
dp = [0]*(n+1)
Max = 0
for i in range(n):
    Max = 0
    for j in range(i):
        if arr[i] > arr[j]:
            Max = max(dp[j], Max)
    dp[i] += Max+1
print(max(dp))

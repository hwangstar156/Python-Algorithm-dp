n, k = map(int, input().split())
arr = [[1]*(n+1) for _ in range(k+1)]
for i in range(1, k+1):
    for j in range(1, n+1):
        arr[i][j] = (arr[i-1][j]+arr[i][j-1]) % 1000000000
print(arr[k][n])

n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
print(arr)
i = 0
ans = 0
while i < n:
    ans += 1
    i += arr[i]

print(ans)

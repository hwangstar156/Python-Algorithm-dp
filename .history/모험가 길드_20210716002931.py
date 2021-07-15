n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
print(arr)
i = 0
ans = 0
while True:
    ans += 1
    if i >= n:
        break
    i += arr[i]

print(ans)

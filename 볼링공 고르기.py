n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = 0
count = [0]*11
for i in arr:
    count[i] += 1

for j in range(1, m+1):
    result += (n-count[j])*count[j]
    n = n-count[j]

print(result)

n = int(input())
arr = []

while True:
    arr.append(n % 10)
    if n == 0:
        break
    n = n//10
arr = arr[::-1]
Sum = arr[0]
for x in range(1, len(arr)):
    Sum = max(Sum+arr[x], Sum*arr[x])

print(Sum)

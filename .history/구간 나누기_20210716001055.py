n = int(input())
arr = []

while True:
    arr.append(n % 10)
    if n == 0:
        break
    n = n/10

print(arr)

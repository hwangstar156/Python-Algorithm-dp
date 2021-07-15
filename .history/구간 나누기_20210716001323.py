n = int(input())
arr = []

while True:
    arr.append(n % 10)
    if n == 0:
        break
    n = n//10

arr = arr[::-1]
print(arr)

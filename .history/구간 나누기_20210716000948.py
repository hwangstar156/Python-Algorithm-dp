n = int(input())
arr = []

while n >= 0:
    arr.append(n % 10)
    n = n//10

print(arr)

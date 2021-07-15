arr = [0]*41
arr[1] = 1
arr[2] = 2
vip = [0]
Sum = 1
n = int(input())
m = int(input())
for _ in range(m):
    vip.append(int(input()))
vip.append(n+1)
for i in range(3, 41):
    arr[i] = arr[i-1]+arr[i-2]

for i in range(len(vip)-1):
    Sum *= arr[vip[i+1]-vip[i]-1]

print(Sum)

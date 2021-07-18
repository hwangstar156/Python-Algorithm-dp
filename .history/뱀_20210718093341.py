n = int(input())
k = int(input())
Point = []
arr = []
for _ in range(k):
    Point.append(list(map(int, input().split())))
l = int(input())
for _ in range(l):
    arr.append(list(input().split()))

Map = [[0 for _ in range(n)]for _ in range(n)]
for point in Point:
    Map[point[0]-1][point[1]-1] = 1
print(Map)

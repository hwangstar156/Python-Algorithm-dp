from copy import deepcopy
from collections import deque
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def turn(now, direction):
    if direction == 'D':
        now += 1
    else:
        now -= 1
    if now == -1:
        now = 3
    elif now == 4:
        now = 0
    return now


n = int(input())
k = int(input())
Point = []
arr = []
now = 0
time = 0
order = 0
x, y = 0, 0
for _ in range(k):
    Point.append(list(map(int, input().split())))
l = int(input())
for _ in range(l):
    arr.append(list(input().split()))
Map = [[0 for _ in range(n)]for _ in range(n)]

visit = deque()
visit.append((0, 0))

for point in Point:
    Map[point[0]-1][point[1]-1] = 1

while True:
    if order < len(arr) and time == int(arr[order][0]):
        now = turn(now, arr[order][1])
        order += 1
    x = x+dx[now]
    y = y+dy[now]
    if x < 0 or y < 0 or x >= n or y >= n or (x, y) in visit:
        break
    if Map[x][y] == 0:
        visit.popleft()
    visit.append((x, y))
    time += 1


print(visit)
print(time)

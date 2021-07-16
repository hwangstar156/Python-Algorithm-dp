dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
Map = []
result = 0
fail = 0
n, m = map(int, input().split())
x, y, location = map(int, input().split())
for _ in range(n):
    Map.append(list(map(int, input().split())))
visit = [[0 for _ in range(n)]for _ in range(m)]


def turnLeft(num):
    k = num-1
    if(k < 0):
        k = 3
    return k


while True:
    if(fail == 4):
        px = x-dx[location]
        py = y-dy[location]
        if(px >= n or px < 0 or py < 0 or py >= m or Map[px][py] == 1):
            print(result)
            break
        visit[px][py] = True
        fail = 0
        x = px
        y = py
    location = turnLeft(location)
    nx = x+dx[location]
    ny = y+dy[location]
    if(nx >= n or nx < 0 or ny < 0 or ny >= m or visit[nx][ny] or Map[nx][ny] == 1):
        fail += 1
        continue
    visit[nx][ny] = True
    fail = 0
    x = nx
    y = ny
    result += 1

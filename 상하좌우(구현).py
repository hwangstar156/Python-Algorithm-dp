n = int(input())
curX = 1
curY = 1

order = list(input().split())

for i in range(len(order)):
    if order[i] == 'L':
        x, y = 0, -1
    elif order[i] == 'R':
        x, y = 0, 1
    elif order[i] == 'U':
        x, y = -1, 0
    elif order[i] == 'D':
        x, y = 1, 0
    if 0 < curX+x <= n and 0 < curY+y <= n:
        curX += x
        curY += y

print(curX, curY, end=' ')

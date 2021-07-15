n = input()
result = 0
dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]
curX = int(n[1])-1
curY = int(ord(n[0]))-int(ord('a'))

for i in range(8):
    nx = curX+dx[i]
    ny = curY+dy[i]

    if 0 <= nx < 8 and 0 <= ny < 8:
        result += 1

print(result)

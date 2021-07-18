
def rotate(key, n):
    temp = [[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[n-j][i] = key[i][j]
    for i in range(n):
        for j in range(n):
            key[i][j] = temp[i][j]


key = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(key, 3)
print(key)

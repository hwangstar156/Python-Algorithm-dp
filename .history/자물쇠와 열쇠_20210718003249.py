

def rotate(key, n):
    temp = [[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[n-j-1][i] = key[i][j]
    for i in range(n):
        for j in range(n):
            key[i][j] = temp[i][j]


def move(lock, m, n):
    temp = [[-1 for _ in range(n+2*(m-1))]for _ in range(n+2*(m-1))]
    for i in range(n):
        for j in range(n):
            temp[i+m-1][j+m-1] = lock[i][j]
    return temp


def check(lock, n, m):
    for i in range(n):
        for j in range(n):
            if lock[i+m-1][j+m-1] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    lock = move(lock, m, n)
    for _ in range(4):
        rotate(key, m)
        for i in range(n+m-1):
            for j in range(n+m-1):
                for k in range(m):
                    for t in range(m):
                        if lock[i+k][j+t] >= 0:
                            lock[i+k][j+t] += key[k][t]
                            if check(lock, n, m):
                                return True
                            lock[i+k][j+t] -= key[k][t]
    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))

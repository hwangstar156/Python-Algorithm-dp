from copy import deepcopy


def rotate(key, n):
    temp = [[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[n-j-1][i] = key[i][j]
    for i in range(n):
        for j in range(n):
            key[i][j] = temp[i][j]


def move(lock, m, n):
    temp = [[-1 for _ in range(n+2*(m-1))]for _ in range(n+2*m)]
    for i in range(n):
        for j in range(n):
            temp[i+m-1][j+m-1] = lock[i][j]
    lock = deepcopy(temp)


lock = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
move(lock, 3, 3)
print(lock)
# def solution(key, lock):
#     n=len(lock)
#     m=len(key)
#     for _ in range(4):
#         rotate(key,m)
#         for i in range(n):
#             for j in range(n):

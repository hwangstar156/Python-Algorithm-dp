n = int(input())
result = 0


def check(num):
    while num > 0:
        if(num % 10 == 3):
            return True
        num = num//10
    return False


for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if check(k) or check(j) or check(i):
                result += 1

print(result)

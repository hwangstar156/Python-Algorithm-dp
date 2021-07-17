n = input()
length = len(n)//2
a1 = n[:length]
a2 = n[length:]
if sum(list(map(int, a1))) == sum(list(map(int, a2))):
    print('LUCKY')
else:
    print('READY')

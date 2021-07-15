n = input()
Sum = 0
arr = []
for i in n:
    if i.isdigit():
        Sum += int(i)
    else:
        arr.append(i)

print(''.join(sorted(arr, key=lambda x: ord(x)))+str(Sum))

n = input()
Sum = 0
arr = ""
for i in n:
    if i.isdigit():
        Sum += int(i)
    else:
        arr += i

sorted(arr)
print(arr)

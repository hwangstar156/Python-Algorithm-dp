Str = input()
count = [0, 0]
for i in range(len(Str)):
    if i+1 == len(Str) or (Str[i] != Str[i+1]):
        count[int(Str[i])] += 1
print(min(count))

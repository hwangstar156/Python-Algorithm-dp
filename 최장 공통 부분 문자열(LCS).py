s1 = input().strip()
s2 = input().strip()
ans = 0

lcs = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]

for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        if s1[i-1] == s2[j-1]:
            lcs[i][j] = lcs[i-1][j-1]+1
            ans = max(ans, lcs[i][j])

print(ans)

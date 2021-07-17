def solution(s):
    length = len(s)
    Min = length
    for i in range(1, (length//2)+1):
        st = 0
        k = ""
        res = length
        for j in range(0, length+1, i):
            save = s[j:j+i]
            if j == length and st >= 2:
                res += -i*st+i+len(str(st))
            elif k == "":
                k = save
            elif k != save:
                if st >= 2:
                    res += -i*st+i+len(str(st))
                k = save
                st = 0
            st += 1
        Min = min(res, Min)
    return Min


s = "a"
print(solution(s))

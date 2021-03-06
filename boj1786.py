def getpi(p):
    m = len(p)
    j = 0
    pi = [0 for i in range(m)]
    for i in range(1, m):
        while j > 0 and p[i] != p[j]:
            j = pi[j-1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j
    return pi

def kmp(s, p):
    ans = []
    pi = getpi(p)
    n = len(s)
    m = len(p)
    j = 0
    for i in range(n):
        while j > 0 and s[i] != p[j]:
            j = pi[j-1]
        if s[i] == p[j]:
            if j == m - 1:
                ans.append(i-m+1)
                j = pi[j]
            else:
                j += 1
    return ans

s = input()
p = input()

matched = kmp(s, p)

print(len(matched))
for i in range(len(matched)):
    print(matched[i] + 1, end=" ")
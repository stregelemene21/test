n, m = map(int,input().split())
s = [i for i in range(1, n+1)]
listResult = [1]
while True:
    for i in range(0, m-1):
        s.append(s.pop(0))
    if s[0] == 1 :
        break
    else :
        listResult.append(s[0])
print(*listResult) 

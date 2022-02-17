import sys

n = sys.argv[1]
m= sys.argv[2]

s = [i for i in range(1, int(n)+1)]
listResult = [1]
while True:
    for i in range(0, int(m)-1):
        s.append(s.pop(0))
    if s[0] == 1 :
        break
    else :
        listResult.append(s[0])
print(*listResult)

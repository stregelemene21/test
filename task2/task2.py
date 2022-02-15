import sys

center = open(sys.argv[1])
points = open(sys.argv[2])

xc = float(center.read(1))
yc = float(center.read(2))
r = float(center.read(3))
def PointInCircle(xc, yc, r, x, y):
    result = ((x-xc)**2+(y-yc)**2) ** 0.5
    if result < r :
        print('1')
    elif result > r:
        print('2')
    else:
        print('0')
        
p = points.readlines()
for i in p:
    x = float(i[0])
    y = float(i[2])
    PointInCircle(xc, yc, r, x, y)

import math
moons = [[ 5,-1, 5, 0, 0, 0], [0, -14, 2,0,0,0], [16, 4, 0,0,0,0], [18, 1, 16,0,0,0]]
start = [[ 5,-1, 5, 0, 0, 0], [0, -14, 2,0,0,0], [16, 4, 0,0,0,0], [18, 1, 16,0,0,0]]

def getcol(matrix, col):
    return [row[col] for row in matrix]

t = 0
xf = False
yf = False
zf = False
while 1:
    t += 1
    for m in moons:
        for sm in moons:
            g = lambda x:(x[0]<x[1])-(x[0]>x[1])
            m[3:6] = list(map(sum, zip(m[3:6], list(map(g,zip(m[0:3],sm[0:3]))))))
    for m in moons:
        m[0:3]=[sum(x) for x in zip(m[0:3],m[3:6])]
        
    if not(xf) and (getcol(moons,0) == getcol(start,0)) and (getcol(moons,3) == getcol(start,3)):
        xf = True
        tx = t
    if not(yf) and (getcol(moons,1) == getcol(start,1)) and (getcol(moons,4) == getcol(start,4)):
        yf = True
        ty = t
    if not(zf) and (getcol(moons,2) == getcol(start,2)) and (getcol(moons,5) == getcol(start,5)):
        zf = True
        tz = t
                                                  
    if xf and yf and zf:
        break

result = (tx*ty*tz)/(math.gcd(tx,ty)*math.gcd(tx*ty,tz))
print(round(result))

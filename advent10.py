from fractions import Fraction

astros = []
with open('astros.txt') as f:
    for line in f:
        astros.append(line[:(-1)])

astrolist = []
for y in range(len(astros)):
    for x in range(len(astros[y])):
        if astros[y][x]=='#':
            astrolist.append([y,x])

def astrocount(pos, dir):
    newpos = list(map(sum, zip(pos, dir)))
    if not(0 <= newpos[1] < len(astros[0])) or not(0 <= newpos[0] < len(astros)):
        return 0
    else:
        return (astros[newpos[0]][newpos[1]]=='#') + astrocount(newpos, dir)


# Return all directions with max step size
def dirs(maxStep):
    directions = []
    maxsq = maxStep*maxStep
    for i in range(maxsq+1):
        fract = Fraction(i/maxsq).limit_denominator(maxStep)
        direction = [fract.numerator, fract.denominator]
        if i==0 or direction != directions[-1]:
            directions.append(direction)
            
    #create full turn
    quart1 = list(map(lambda x:[-x[1],x[0]],directions)) + list(map(lambda x:[-x[0],x[1]],reversed(directions[:-1])))
    quart2 = list(map(lambda x:[x[0],x[1]],directions[1:])) + list(map(lambda x:[x[1],x[0]],reversed(directions[:-1])))
    quart3 = list(map(lambda x:[x[1],-x[0]],directions[1:])) + list(map(lambda x:[x[0],-x[1]],reversed(directions[:-1])))
    quart4 = list(map(lambda x:[-x[0],-x[1]],directions[1:])) + list(map(lambda x:[-x[1],-x[0]],reversed(directions[1:-1])))
    return quart1+quart2+quart3+quart4


# Task 1
obfulist = []
for pos in astrolist:
    dircount=[]
    for drs in dirs(11):
        dircount.append(astrocount(pos,drs))
    obfulist.append( sum(map(lambda x:0 if x==0 else x-1, dircount)))
                   
print(len(astrolist)-min(obfulist)-1)


# Task 2
def zap(pos, dir):
    newpos = list(map(sum, zip(pos, dir)))
    if not(0 <= newpos[1] < len(astros[0])) or not(0 <= newpos[0] < len(astros)):
        return []
    elif astros[newpos[0]][newpos[1]]=='#':
        return newpos
    elif astros[newpos[0]][newpos[1]]=='.':
        return zap(newpos, dir)

zapped = []
laserpos = astrolist[obfulist.index(min(obfulist))]
for drs in dirs(23):
    laserhit = zap(laserpos,drs)
    if laserhit != []:
        zapped.append(laserhit)

print(zapped[199][1]*100+zapped[199][0])

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


# This gave the right answer, but is still wrong!!!
directions = []
for y in range(-11,12):
    for x in range(-11,12):
        if (abs(x)==1 or
            abs(y)==1 or
            abs(x-y)==1 or
            (abs(x)>1 and 
             abs(y)>1 and
             ((x-y)%x) and
             ((x-y)%y) and
             (x%(x-y)) and
             (y%(x-y)) and
             (x%y) and
             (y%x)
             )):
            directions.append([y,x])
             

obfulist = []
for pos in astrolist:
    dircount=[]
    for dirs in directions:
        dircount.append(astrocount(pos,dirs))
    obfulist.append( sum(map(lambda x:0 if x==0 else x-1, dircount)))
                   
print(len(astrolist)-min(obfulist)-1)

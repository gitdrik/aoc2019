import copy

Eris = [];
with open('24.txt') as f:
    for line in f:
        for c in line.strip():
            Eris.append(c == '#')

startEris = copy.deepcopy(Eris)

# Part 1
bds = set()
bd = sum([b << i for i, b in enumerate(Eris)])

while not(bd in bds):
    bds.add(bd)
    n = []
    for p in range(len(Eris)):
        sp = 0
        if p%5:
            sp += Eris[p-1]
        if (p+1)%5:
            sp += Eris[p+1]
        if p > 4:
            sp += Eris[p-5]
        if p < 20:
            sp += Eris[p+5]
        if ((Eris[p] and sp == 1) or
            (not(Eris[p]) and (sp in [1,2]))):
            n.append(True)
        else:
            n.append(False)
    Eris = n
    bd = sum([b << i for i, b in enumerate(Eris)])

print(bd)

# Part 2
plutoEris = [[0]*25 for i in range(205)]
plutoEris[102] = list(map(int,startEris))

for t in range(200):
    nextPE = []
    for l in range(1,204):
        nextLayer = []
        for p in range(25):
            psum = 0
            
            # Up
            if p < 5:
                psum += plutoEris[l-1][7]
            elif p == 17:
                psum += sum(plutoEris[l+1][20:25])
            elif p != 12:
                psum += plutoEris[l][p-5]
                
            # Right
            if not((p+1)%5):
                psum += plutoEris[l-1][13]
            elif p == 11:
                psum += sum([plutoEris[l+1][x] for x in [0,5,10,15,20]])
            elif p != 12:
                psum += plutoEris[l][p+1]

            # Down
            if p > 19:
                psum += plutoEris[l-1][17]
            elif p == 7:
                psum += sum(plutoEris[l+1][0:5])
            elif p != 12:
                psum += plutoEris[l][p+5]

            # Left
            if not(p%5):
                psum += plutoEris[l-1][11]
            elif p == 13:
                psum += sum([plutoEris[l+1][x] for x in [4,9,14,19,24]])
            elif p != 12:
                psum += plutoEris[l][p-1]

            if ((plutoEris[l][p] and psum == 1) or
                (not(plutoEris[l][p]) and (psum in [1,2]))):
                nextLayer.append(1)
            else:
                nextLayer.append(0)
                
        nextPE.append(nextLayer)
        
    plutoEris = [[0]*25] + nextPE + [[0]*25]
     
print(sum([sum(x) for x in plutoEris]))


import math

with open('18.txt') as f:
   caveraw = f.read().strip()

chars = set(caveraw)
small = chars & {chr(x) for x in range(ord('a'),ord('z')+1)}
big = chars & {chr(x) for x in range(ord('A'),ord('Z')+1)}
cave = list(map(list,caveraw.split('\n')))

# Close the quartermazes
cave[39][40] = '#'
cave[40][39:42] = ['#','#','#']
cave[41][40] = '#'
#for l in [''.join(c) for c in cave]:print(l)

def graph(prevpos, pos, prevnode, steps, cave):
    nodes = {}
    moves = [(pos[0]-1,pos[1]),(pos[0],pos[1]+1),
             (pos[0]+1,pos[1]),(pos[0],pos[1]-1)]
    moves = list(filter(lambda x:x!=prevpos, moves))
    moves = list(filter(lambda x:cave[x[0]][x[1]]!='#', moves))

    if (cave[pos[0]][pos[1]] != '.' or len(moves) > 1):
        nodes[pos] = {}
        if prevnode != pos:
            nodes[pos][prevnode] = steps
        prevnode = pos
        steps = 0

    for m in moves:
        nodes.update(graph(pos, m, prevnode,steps+1,cave))
  
    return nodes

# Make unidirectional graph bi-directional
def bidi(g):
    for n in g:
        for m in g[n]:
            g[m].update({n:g[n][m]})
    return g

# Make four graphs
g1 = bidi(graph((39,39),(39,39),(39,39),0,cave))
g2 = bidi(graph((39,41),(39,41),(39,41),0,cave))
g3 = bidi(graph((41,39),(41,39),(41,39),0,cave))
g4 = bidi(graph((41,41),(41,41),(41,41),0,cave))

# Extract nodes with keys and doors
keynodes = set()
doornodes = set()
for n in {**g1, **g2, **g3, **g4}:
    if cave[n[0]][n[1]] in small:
        keynodes.update({n})
    if cave[n[0]][n[1]] in big:
        doornodes.update({n})
        
# Link keys to doors and doors to keys
keydoors = {}
doorkeys = {}
for n in {**g1, **g2, **g3, **g4}:
    if cave[n[0]][n[1]] in big:
        for k in keynodes:
            if cave[n[0]][n[1]].lower() == cave[k[0]][k[1]]:
                keydoors[k] = n
                doorkeys[n] = k

def dijkstra(start, stop, g):
    pos = start
    PL = {pos:0}
    TL = {}
    SP = {}
    SP[start] = [start]
    while pos != stop:
        for n in g[pos]:
            if (n not in PL): #and (n not in lockeddoors) and (n not in blockingkeys):
                if n in TL:
                    newTL = PL[pos] + g[pos][n]
                    if newTL < TL[n]:
                        TL[n] = newTL
                        print(SP)
                        SP[n] = SP[pos] + [n]
                else:
                    TL[n] = PL[pos] + g[pos][n]
                    SP[n] = SP[pos] + [n]
        if TL != {}:
            pos = min(TL, key=TL.get)
            PL[pos]=TL[pos]
            del TL[pos]
        else:
            return math.inf
    return (PL[pos], SP[pos])

# Make graphs with precalculated steps from all keys to all keys,
# with keys and doors in between, starting from start.
def makeG(g, start):
    global keynodes
    global doornodes
    G = {}
    for n in {x for x in keynodes | {start} if x in g}:
        G[n] = {}
        for m in {x for x in keynodes | {start} if x in g}:
            (steps, route) = dijkstra(n,m,g)
            route = route[1:-1]
            G[n][m] = [steps,
                       {x for x in route if x in keynodes},
                       {x for x in route if x in doornodes}]
    return G

G1 = makeG(g1,(39,39))
G2 = makeG(g2,(39,41))
G3 = makeG(g3,(41,39))
G4 = makeG(g4,(41,41))

def quatrofetch(n1, n2, n3, n4, rkeyn, steps, maxsteps, G1, G2, G3, G4):
    if len(rkeyn) == 0:
        print(steps)
        return steps 
    for knode in rkeyn:
        if ((knode in G1[n1]) and
            (steps + G1[n1][knode][0] < maxsteps) and
            (len(G1[n1][knode][1] & rkeyn) == 0) and
            (len(G1[n1][knode][2] & {keydoors[x] for x in rkeyn})==0)):
            maxsteps = min(maxsteps,
                           quatrofetch(knode,n2,n3,n4, rkeyn-{knode}, steps+G1[n1][knode][0],maxsteps,G1,G2,G3,G4))
        elif ((knode in G2[n2]) and
              (steps + G2[n2][knode][0] < maxsteps) and
              (len(G2[n2][knode][1] & rkeyn) == 0) and
              (len(G2[n2][knode][2] & {keydoors[x] for x in rkeyn})==0)):
            maxsteps = min(maxsteps,
                           quatrofetch(n1,knode,n3,n4, rkeyn-{knode}, steps+G2[n2][knode][0],maxsteps,G1,G2,G3,G4))
        elif ((knode in G3[n3]) and
              (steps + G3[n3][knode][0] < maxsteps) and
              (len(G3[n3][knode][1] & rkeyn) == 0) and
              (len(G3[n3][knode][2] & {keydoors[x] for x in rkeyn})==0)):
            maxsteps = min(maxsteps,
                           quatrofetch(n1,n2,knode,n4, rkeyn-{knode}, steps+G3[n3][knode][0],maxsteps,G1,G2,G3,G4))
        elif ((knode in G4[n4]) and
              (steps + G4[n4][knode][0] < maxsteps) and
              (len(G4[n4][knode][1] & rkeyn) == 0) and
              (len(G4[n4][knode][2] & {keydoors[x] for x in rkeyn})==0)):
            maxsteps = min(maxsteps,
                           quatrofetch(n1,n2,n3,knode, rkeyn-{knode}, steps+G4[n4][knode][0],maxsteps,G1,G2,G3,G4))
    return maxsteps

print(quatrofetch((39,39),(39,41),(41,39),(41,41),keynodes,0,math.inf,G1,G2,G3,G4))

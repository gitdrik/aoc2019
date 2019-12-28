import math

with open('18.txt') as f:
   caveraw = f.read().strip()

chars = set(caveraw)
small = chars & {chr(x) for x in range(ord('a'),ord('z')+1)}
big = chars & {chr(x) for x in range(ord('A'),ord('Z')+1)}
cave = list(map(list,caveraw.split('\n')))

# Close the quartermazes
cave[39][40] = '#'
cave[40][39:42] = ['#','@','#']
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

# Make a graph of the cave
cavegraph = graph((39,39),(39,39),(39,39),0,cave)
cavegraph.update(graph((39,41),(39,41),(39,41),0,cave))
cavegraph.update(graph((41,39),(41,39),(41,39),0,cave))
cavegraph.update(graph((41,41),(41,41),(41,41),0,cave))

# manually connect quartermazes and add centernode
cavegraph[(39,39)].update({(39,41):2, (41,39):2, (40,40):2})
cavegraph[(39,41)].update({(39,39):2, (41,41):2, (40,40):2})
cavegraph[(41,39)].update({(39,39):2, (41,41):2, (40,40):2})
cavegraph[(41,41)].update({(41,39):2, (39,41):2, (40,40):2})
cavegraph[(40,40)] = {(39,39):2, (39,41):2, (41,39):2, (41,41):2}
cnodes = {(40,40),(39,39),(39,41),(41,39),(41,41)}

# Make graph bi-directional
for n in cavegraph:
    for m in cavegraph[n]:
        cavegraph[m].update({n:cavegraph[n][m]})


keynodes = set()
doornodes = set()
for n in cavegraph:
    if cave[n[0]][n[1]] in small:
        keynodes.update({n})
    if cave[n[0]][n[1]] in big:
        doornodes.update({n})

keydoors = {}
doorkeys = {}
for n in cavegraph:
    if cave[n[0]][n[1]] in big:
        for k in keynodes:
            if cave[n[0]][n[1]].lower() == cave[k[0]][k[1]]:
                keydoors[k] = n
                doorkeys[n] = k

def dijkstra(start, stop):
    global cavegraph
    pos = start
    PL = {pos:0}
    TL = {}
    SP = {}
    SP[start] = [start]
    while pos != stop:
        for n in cavegraph[pos]:
            if (n not in PL): #and (n not in lockeddoors) and (n not in blockingkeys):
                if n in TL:
                    newTL = PL[pos] + cavegraph[pos][n]
                    if newTL < TL[n]:
                        TL[n] = newTL
                        print(SP)
                        SP[n] = SP[pos] + [n]
                else:
                    TL[n] = PL[pos] + cavegraph[pos][n]
                    SP[n] = SP[pos] + [n]
        if TL != {}:
            pos = min(TL)
            PL[pos]=TL[pos]
            del TL[pos]
        else:
            return math.inf
    return (PL[pos], SP[pos])

# Make graph with precalculated steps from all keys to all keys,
# with keys and doors in between, and starting also from center (40,40).
G = {}
for n in keynodes | {(40,40)}:
    G[n] = {}
    for m in keynodes:
        (steps, route) = dijkstra(n,m)
        route = route[1:-1]
        G[n][m] = [steps,
                   {x for x in route if x in keynodes},
                   {x for x in route if x in doornodes}]

def fetch(node, rkeyn, steps, maxsteps, G):
    if len(rkeyn) == 0:
        print(steps)
        return steps 
    for knode in rkeyn:
        if ((steps + G[node][knode][0] < maxsteps) and
            (len(G[node][knode][1] & rkeyn) == 0) and
            (len(G[node][knode][2] & {keydoors[x] for x in rkeyn})==0)):
            maxsteps = min(maxsteps,
                           fetch(knode, rkeyn-{knode}, steps+G[node][knode][0],maxsteps,G))
    return maxsteps

print(fetch((40,40),keynodes,0,math.inf,G)) # right answer: 4620

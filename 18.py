import math
import copy

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

# Remove dead ends
while 1:
    dels = []
    for n in cavegraph:
        if cave[n[0]][n[1]]=='.' and len(cavegraph[n]) == 1:
            dels.append(n)
    if len(dels):
        for n in dels:
            del cavegraph[n]
        for n in cavegraph:
            for m in dels:
                if m in cavegraph[n]:
                    del cavegraph[n][m]        
    else:
        break

keynodes = set()
for n in cavegraph:
    if cave[n[0]][n[1]] in small:
        keynodes.update({n})

keydoors = {}
for n in cavegraph:
    if cave[n[0]][n[1]] in big:
        for k in keynodes:
            if cave[n[0]][n[1]].lower() == cave[k[0]][k[1]]:
                keydoors[k] = n


def dijkstra(start, stop, lockeddoors):
    global cavegraph
    pos = start
    PL = {pos:0}
    TL = {}
    SP = set()
    while pos != stop:
        for n in cavegraph[pos]:
            if (n not in PL) and (n not in lockeddoors):
                if n in TL:
                    TL[n] = min(TL[n], PL[pos] + cavegraph[pos][n])
                else:
                    TL[n] = PL[pos] + cavegraph[pos][n]
        if TL != {}:
            pos = min(TL)
            PL[pos]=TL[pos]
            del TL[pos]
        else:
            return math.inf
    return PL[pos]


def fetchkeys(node, remainingkeynodes, steps, maxsteps):
    global cavegraph
    global keydoors
    global small
    global big
    
    if steps >= maxsteps:
        return math.inf

    if remainingkeynodes == set():
        print(steps)
        return steps

    lockeddoors = {keydoors[x] for x in remainingkeynodes}
    
    for knode in remainingkeynodes:
        knodesteps = dijkstra(node, knode, lockeddoors)
        if steps+knodesteps < maxsteps:
            maxsteps = min(maxsteps,
                       fetchkeys(knode, copy.deepcopy(remainingkeynodes-{knode}),
                                 steps+knodesteps,maxsteps))
    return maxsteps


print(fetchkeys((40,40), keynodes, 0, math.inf))
                   
# 7896, 6250, 5646 was to high.
# 4636, 5216 was wrong.
# not 302
# 4868 was righ for someone else!!!



    

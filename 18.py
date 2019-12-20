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
for l in [''.join(c) for c in cave]:print(l)


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
cavegraph.update(graph((41,41),(41,41),(41,41),0,cave))
cavegraph.update(graph((41,39),(41,39),(41,39),0,cave))

# Make graph bi-directional
for n in cavegraph:
    for m in cavegraph[n]:
        cavegraph[m].update({n:cavegraph[n][m]})

# Remove dead ends
while 1:
    delitems = []
    for n in cavegraph:
        if cave[n[0]][n[1]]=='.' and len(cavegraph[n]) == 1:
            delitems.append(n)
    if len(delitems):
        for i in delitems:
            del cavegraph[i]
    else:
        break

# manually connect quartermazes
cavegraph[(39,39)] = {(39,41):2, (41,39):2, (41,41):4}
cavegraph[(39,41)] = {(39,39):2, (41,39):4, (41,41):2}
cavegraph[(41,39)] = {(39,41):4, (39,39):2, (41,41):4}
cavegraph[(41,41)] = {(39,39):4, (41,39):2, (39,41):4}
cnodes = {(39,39),(39,41),(41,39),(41,42)}
  
def fetchkeys(node, prevnode, keys, steps):
    global cavegraph
    global small
    global big
    foundkey = False
    obj = cave[node[0]][node[1]]
    if (obj in small) and not(obj in keys):
        keys.update(cave[node[0]][node[1]])
        if len(keys)==len(small):
            return steps
        foundkey = True

    nextnodes = []
    for n in cavegraph[node]:
        # if not (closeddoor or (direction we came from but no found key) or (from special nodes))
        if not(((cave[n[0]][n[1]] in big) and (cave[n[0]][n[1]].lower() not in keys)) or
               (n == prevnode and not(foundkey) or
               ((prevnode in cnodes) and (n in cnodes))):
            nextnodes.append(n)

    nextsteps = math.inf
    for n in nextnodes:
        nextsteps = min(nextsteps, fetchkeys(n, node, keys, steps+cavegraph[node][n]))

    return nextsteps

print(min(fetchkeys((39,39),(39,39),set(),2),
          fetchkeys((39,41),(39,41),set(),2),
          fetchkeys((41,39),(41,39),set(),2),
          fetchkeys((41,41),(41,41),set(),2))


    

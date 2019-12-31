import math

maze = []
with open('20.txt') as f:
    for line in f:
        maze += [line.strip('\n')]

outer = {}
inner = {}
# top
for i, c in enumerate(maze[0]):
    if c in {chr(x) for x in range(ord('A'),ord('Z')+1)}:
        outer[2,i] = ''.join([maze[0][i],maze[1][i]])
# inner top
for i, c in enumerate(maze[37]):
    if c in {chr(x) for x in range(ord('A'),ord('Z')+1)}:
        inner[36,i] = ''.join([maze[37][i],maze[38][i]])
# inner bottom
for i, c in enumerate(maze[92]):
    if c in {chr(x) for x in range(ord('A'),ord('Z')+1)}:
        inner[94,i] = ''.join([maze[92][i],maze[93][i]])
# bottom
for i, c in enumerate(maze[129]):
    if c in {chr(x) for x in range(ord('A'),ord('Z')+1)}:
        outer[128,i] = ''.join([maze[129][i],maze[130][i]])
# left
for i, c in enumerate([x[0] for x in maze]):
    if c in {chr(x) for x in range(ord('A'),ord('Z')+1)}:
        outer[i,2] = ''.join([maze[i][0],maze[i][1]])
# inner left
for i, c in enumerate([x[37] for x in maze]):
    if c in {chr(x) for x in range(ord('A'),ord('Z')+1)}:
        inner[i,36] = ''.join([maze[i][37],maze[i][38]])
# inner right
for i, c in enumerate([x[92] for x in maze]):
    if c in {chr(x) for x in range(ord('A'),ord('Z')+1)}:
        inner[i,94] = ''.join([maze[i][92],maze[i][93]])
# right
for i, c in enumerate([x[129] for x in maze]):
    if c in {chr(x) for x in range(ord('A'),ord('Z')+1)}:
        outer[i,128] = ''.join([maze[i][129],maze[i][130]])


# Makes some sort of graph
def graph(prevpos, pos, prevnode, steps, maze, labels):
    nodes = {}
    moves = [(pos[0]-1,pos[1]),(pos[0],pos[1]+1),
             (pos[0]+1,pos[1]),(pos[0],pos[1]-1)]
    moves = [x for x in moves if x != prevpos]
    moves = [x for x in moves if maze[x[0]][x[1]] != '#']

    if (len(moves) > 1) or (pos in labels):
        nodes[pos] = {}
        if prevnode != pos:
            nodes[pos][prevnode] = steps
        prevnode = pos
        steps = 0
    moves = [x for x in moves if maze[x[0]][x[1]] == '.']
    for m in moves:
        nodes.update(graph(pos, m, prevnode,steps+1,maze,labels))
  
    return nodes

# Make graph bi-directional
def bidi(g):
    for n in g:
        for m in g[n]:
            g[m].update({n:g[n][m]})
    return g

# special dijkstra with infinite recursion awareness
def dijkstra(start,stop,inodes,onodes,links,g):
    pos = start
    PL = {pos:0}
    TL = {}
    #SP = {}
    #SP[start] = [start]
    while pos != stop:
        nexts = {}
        for n in g[pos[0:2]]:
            nexts[(*n,pos[2])] = g[pos[0:2]][n]
        # Check if layer traversal is possible
        if pos[0:2] in onodes and pos[2] > 0:
            nexts[(*links[pos[0:2]],pos[2]-1)] = 1
        elif pos[0:2] in inodes:
            nexts[(*links[pos[0:2]],pos[2]+1)] = 1
        for n in nexts:
            if (n not in PL):
                if n in TL:
                    newTL = PL[pos] + nexts[n]
                    if newTL < TL[n]:
                        TL[n] = newTL
                        #SP[n] = SP[pos] + [n]
                else:
                    TL[n] = PL[pos] + nexts[n]
                    #SP[n] = SP[pos] + [n]
        if TL != {}:
            pos = min(TL, key=TL.get)
            PL[pos]=TL[pos]
            del TL[pos]
        else:
            return math.inf
    return (PL[pos]) #, SP[pos])


# Create a coherent graph of the whole maze
G = {}
for p in {**outer, **inner}:
    if p not in G:
        G.update(bidi(graph(p,p,p,0,maze,{**outer, **inner})))

# Link outer and inner
links = {}
for o in outer:
    for i in inner:
        if outer[o] == inner[i]:
            links[o] = i
            links[i] = o
  
start = (45,128,0)
stop = (128,81,0)
innernodes = set(inner.keys())
outernodes = set(outer.keys()) - {(45,128),(128,81)}
print(dijkstra(start,stop,innernodes,outernodes,links,G))

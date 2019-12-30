import math

maze = []
with open('20.txt') as f:
    for line in f:
        maze += [line.strip('\n')]

#for l in [''.join(str(i) + c) for i, c in enumerate(maze)]:print(l)
#for l in [''.join(c) for i, c in enumerate(maze)]:print(l)

labels = {}
# top
for i, c in enumerate(maze[0]):
    if c in {chr(x) for x in range(ord('A'),ord('Z')+1)}:
        labels[(2,i)] = ''.join([maze[0][i],maze[1][i]])
# inner top
for i, c in enumerate(maze[37]):
    if c in {chr(x) for x in range(ord('A'),ord('Z')+1)}:
        labels[(36,i)] = ''.join([maze[37][i],maze[38][i]])
# inner bottom
for i, c in enumerate(maze[92]):
    if c in {chr(x) for x in range(ord('A'),ord('Z')+1)}:
        labels[(94,i)] = ''.join([maze[92][i],maze[93][i]])
# bottom
for i, c in enumerate(maze[129]):
    if c in {chr(x) for x in range(ord('A'),ord('Z')+1)}:
        labels[(128,i)] = ''.join([maze[129][i],maze[130][i]])
# left
for i, c in enumerate([x[0] for x in maze]):
    if c in {chr(x) for x in range(ord('A'),ord('Z')+1)}:
        labels[(i,2)] = ''.join([maze[i][0],maze[i][1]])
# inner left
for i, c in enumerate([x[37] for x in maze]):
    if c in {chr(x) for x in range(ord('A'),ord('Z')+1)}:
        labels[(i,36)] = ''.join([maze[i][37],maze[i][38]])
# inner right
for i, c in enumerate([x[92] for x in maze]):
    if c in {chr(x) for x in range(ord('A'),ord('Z')+1)}:
        labels[(i,94)] = ''.join([maze[i][92],maze[i][93]])
# right
for i, c in enumerate([x[129] for x in maze]):
    if c in {chr(x) for x in range(ord('A'),ord('Z')+1)}:
        labels[(i,128)] = ''.join([maze[i][129],maze[i][130]])


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

# Dijkstra from Beta
def dijkstra(start, stop, g):
    pos = start
    PL = {pos:0}
    TL = {}
    SP = {}
    SP[start] = [start]
    while pos != stop:
        for n in g[pos]:
            if (n not in PL):
                if n in TL:
                    newTL = PL[pos] + g[pos][n]
                    if newTL < TL[n]:
                        TL[n] = newTL
                        SP[n] = SP[pos] + [n]
                else:
                    TL[n] = PL[pos] + g[pos][n]
                    SP[n] = SP[pos] + [n]
        if TL != {}:
            pos = min(TL)
            PL[pos]=TL[pos]
            del TL[pos]
        else:
            return math.inf
    return (PL[pos], SP[pos])


# Create a coherent graph of the whole maze
G = {}
for p in labels:
    if p not in G:
        G.update(bidi(graph(p,p,p,0,maze,labels)))

# Connect nodes with same label
for l in set(labels.values()):
    ns = [n for n in labels if labels[n]==l]
    if len(ns) > 1:
        G[ns[0]][ns[1]] = 1
        G[ns[1]][ns[0]] = 1

start = [n for n in labels if labels[n]=='AA']
stop = [n for n in labels if labels[n]=='ZZ']

print(dijkstra(start[0],stop[0], G)[0])

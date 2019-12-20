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

# for l in [''.join(c) for c in cave]:print(l)

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

cavegraph = graph((39,39),(39,39),(39,39),0,cave)
cavegraph.update(graph((39,41),(39,41),(39,41),0,cave))
cavegraph.update(graph((41,41),(41,41),(41,41),0,cave))
cavegraph.update(graph((41,39),(41,39),(41,39),0,cave))
    



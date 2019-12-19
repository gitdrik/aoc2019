with open('18.txt') as f:
   caveraw = f.read().strip()

chars = set(caveraw)
small = chars & {chr(x) for x in range(ord('a'),ord('z')+1)}
big = chars & {chr(x) for x in range(ord('A'),ord('Z')+1)}

cave = caveraw.split('\n')

q1 = [x[:41] for x in cave[:41]]
q2 = [x[:41] for x in cave[:41]]


def graph(y,x,cave):
    pass

cavegraph = graph(39,39,q1)
cavegraph += graph(39,41,q2)
cavegraph += graph(41,41,q3)
cavegraph += graph(41,39,q4)
    



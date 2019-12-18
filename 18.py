with open('18.txt') as f:
   caveraw = f.read().strip()

chars = set(caveraw)
small = chars & {chr(x) for x in range(ord('a'),ord('z')+1)}
big = chars & {chr(x) for x in range(ord('A'),ord('Z')+1)}
cave = caveraw.split('\n')



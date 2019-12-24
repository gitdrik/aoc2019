Eris = [];
with open('24.txt') as f:
    for line in f:
        for c in line.strip():
            Eris.append(c == '#')

bds = set()
bd = int(''.join(str(int(i)) for i in reversed(Eris)), 2)

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
    bd = sum([b << i for i, b in enumerate(Eris)]


print(bd)


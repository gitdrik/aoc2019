
orbs = []

with open('orbs.txt') as f:
    for line in f:
        orbs.append([line[0:3],line[4:7]])

def orbcount(mom, depth):
    counts = depth
    for child in list(filter(lambda x:x[0]==mom, orbs)):
        counts += orbcount(child[1], depth+1)
    return counts

print(orbcount('COM', 0))

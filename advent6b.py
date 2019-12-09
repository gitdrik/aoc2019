import math

orbs = []
with open('orbs.txt') as f:
    for line in f:
        orbs.append([line[0:3],line[4:7]])

def dist(a,b,tree):
    if a==b:
        return 0
    distance = math.inf
    for relative in list(filter(lambda x:a in x, tree)):
        distance = min(distance, dist(list(filter(lambda x:x!=a,relative))[0],b,list(filter(lambda x:not(a in x),tree))))
    return distance + 1
    
print(dist('YOU','SAN',orbs)-2)

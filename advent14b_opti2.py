import copy

chemicals = {}
with open('reactions.txt') as f:
    for line in f:
        line = line.replace(',','')
        words = line.split()
        reactants = []
        for i in range((len(words)-3)//2):
            reactants.append((words[i*2+1],int(words[i*2])))
        chemicals[words[-1]] = [0, int(words[-2]), reactants]
start = copy.deepcopy(chemicals)


def produce(chemical, num):
    if chemical == 'ORE':
        return num
    if chemicals[chemical][0] >= num:
        chemicals[chemical][0] -= num
        return 0
    else:
        ore = 0
        need = num - chemicals[chemical][0]
        get = chemicals[chemical][1]
        kits = -(-need // get)
        for chem in chemicals[chemical][2]:
            ore += produce(chem[0],chem[1]*kits)
        chemicals[chemical][0] += chemicals[chemical][1]*kits - num
        return ore

ore = 0
guess = 1000000
while 1:
    ore = produce('FUEL',guess)
    chemicals = copy.deepcopy(start)
    newguess = guess + (1000000000000-ore)*guess//(2*ore)
    if newguess > guess:
        guess = newguess
    else:
        print(guess)
        break

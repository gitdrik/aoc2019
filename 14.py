chemicals = {}
with open('reactions.txt') as f:
    for line in f:
        line = line.replace(',','')
        words = line.split()
        reactants = []
        for i in range((len(words)-3)//2):
            reactants.append((words[i*2+1],int(words[i*2])))
        chemicals[words[-1]] = [0, int(words[-2]), reactants]
chemicals['ORE'] = [0, 0, []]

def produce(chemical, num):
    if chemical == 'ORE':
        chemicals['ORE'][1] += num
        chemicals['ORE'][0] = num
        return
    
    while chemicals[chemical][0] < num:
        for chem in chemicals[chemical][2]:
            produce(chem[0],chem[1])
        chemicals[chemical][0] += chemicals[chemical][1]
        
    chemicals[chemical][0] -= num
    return

produce('FUEL',1)
print(chemicals['ORE'][1])

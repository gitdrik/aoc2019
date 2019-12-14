chemicals = {}
with open('reactions.txt') as f:
    for line in f:
        line = line.replace(',','')
        words = line.split()
        reactants = []
        for i in range((len(words)-3)//2):
            reactants.append((words[i*2+1],int(words[i*2])))
        chemicals[words[-1]] = [0, int(words[-2]), reactants]
chemicals['ORE'] = [1000000000000, 0, []]


def produce(chemical, num, batchsize):
    if chemical == 'ORE':
        if chemicals['ORE'][0] < num*batchsize:
            return False
        chemicals['ORE'][0] -= num*batchsize
        return True
    
    while chemicals[chemical][0] < num*batchsize:
        success = True
        for chem in chemicals[chemical][2]:
            success = success and produce(chem[0],chem[1],batchsize)
        if success:
            chemicals[chemical][0] += chemicals[chemical][1]*batchsize
        else:
            return False
    
    chemicals[chemical][0] -= num*batchsize
    return True


fuel = 0
batchsize = 100000
while produce('FUEL',1, batchsize):
    fuel += batchsize
    batchsize = max(1, chemicals['ORE'][0] // 10000000)

print(fuel)
        
        

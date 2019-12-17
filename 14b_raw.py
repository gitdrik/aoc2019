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

def produce(chemical, num):
    if chemical == 'ORE':
        if chemicals['ORE'][0] < num:
            return False
        chemicals['ORE'][0] -= num
        return True
    
    while chemicals[chemical][0] < num:
        success = True
        for chem in chemicals[chemical][2]:
            success = success and produce(chem[0],chem[1])
        if success:
            chemicals[chemical][0] += chemicals[chemical][1]
        else:
            return False
    
    chemicals[chemical][0] -= num
    return True

fuel = 0;
while produce('FUEL',1):
    fuel +=1
    if not(fuel % 1000):
        opf = (1000000000000-chemicals['ORE'][0]) // fuel
        print(1000000000000//opf)
    



        
        

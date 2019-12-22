code = [];
with open('22.txt') as f:
    for line in f:
        line = line.strip().rsplit(' ',1)
        if  line[1] == 'stack':
            code.append(['deal into new stack',[]])
        else:
            code.append([line[0],int(line[1])])
        

def shuffle(code, deck):
    for c in code:
        if c[0] == 'deal into new stack':
            deck.reverse()
        elif c[0] == 'cut':
            deck = deck[c[1]:] + deck[:c[1]]
        elif c[0] == 'deal with increment':
            ndeck = [0] * len(deck)
            for i in range(len(deck)):
                ndeck[i*c[1] % len(deck)] = deck[i]
            deck = ndeck
            
    return deck


print(shuffle(code,[x for x in range(10007)]).index(2019))
            
            

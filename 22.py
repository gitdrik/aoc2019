code = [];
with open('22.txt') as f:
    for line in f:
        line = line.strip().rsplit(' ',1)
        if  line[1] == 'stack':
            code.append(['deal into new stack',[]])
        else:
            code.append([line[0],int(line[1])])
        
# Part 1
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

# Part 2
def coeffs(code,decklength):
    a,b = 1,0
    for c in reversed(code):
        if c[0] == 'deal into new stack':
            a = -a
            b = -b-1
        elif c[0] == 'cut':
            b = (b + c[1]) % decklength
        elif c[0] == 'deal with increment':
            #only works for prime number decklengths
            a = a * pow(c[1],-1,decklength) % decklength
            b = b * pow(c[1],-1,decklength) % decklength
    return a,b

def polypow(a,b,unshuffles,decklength):
    if unshuffles==0:
        return 1,0
    if unshuffles%2==0:
        return polypow(a*a%decklength, (a*b+b)%decklength, unshuffles//2, decklength)
    else:
        c,d = polypow(a, b, unshuffles-1, decklength)
        return a*c%decklength, (a*d+b)%decklength

def unshuffle(decklength, pos, unshuffles, code):
    a,b = coeffs(code,decklength)
    a,b = polypow(a,b, unshuffles, decklength)
    return (pos*a+b)%decklength

decklength = 119315717514047
unshuffles = 101741582076661
pos = 2020

#Test: part one backwards should give pos 2019 after one unshuffle
#decklength = 10007
#pos = 7614
#unshuffles = 1

print(unshuffle(decklength, pos, unshuffles, code))

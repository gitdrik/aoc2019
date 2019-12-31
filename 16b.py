with open('16.txt') as f:
    s = f.read().strip()

digs = [int(x) for x in s]
offset = int(s[0:7])
roffset = 10000*len(digs)-offset
digs.reverse()
long = digs*(roffset//len(digs)) + digs[:(roffset % len(digs))]

for p in range(100):
    phase = [long[0]]
    for i in range(1,len(long)): 
        phase.append((phase[i-1]+long[i]) % 10)
    long = phase

result = long[-8:]
result.reverse()
print(''.join(map(str, result)))

import copy

CODE = [];
with open('19.txt') as f:
    nums = f.read().strip().split(',')
    for n in nums:
        CODE.append(int(n))
            
# Extend memmory "alot"
CODE += [0]*10*len(CODE)

def intcom(C, pos, relpos, Input, running):
    Output = []

    def read(pos, mode):
        if mode == 0:
            return C[C[pos]]
        elif mode == 1:
            return C[pos]
        elif mode == 2:
            return C[C[pos]+relpos]
    
    def write(val, pos, mode):
        if mode == 0:
            C[C[pos]] = val
        if mode == 2:
            C[C[pos]+relpos] = val

    while running:
        oc = C[pos] % 100
        ma = (C[pos] - oc) // 100 % 10
        mb = (C[pos] - oc - ma*100) // 1000 % 10
        mc = (C[pos] - oc - ma*100 - mb*1000) // 10000 % 10

        if oc == 99:
            return (C, pos, relpos, Output, False)
        
        if oc == 1:
            a = read(pos+1, ma)
            b = read(pos+2, mb)
            write(a + b, pos+3, mc)
            step = 4
            
        elif oc == 2:
            a = read(pos+1, ma)
            b = read(pos+2, mb)
            write(a * b, pos+3, mc)
            step = 4
            
        elif oc == 3:
            if Input == []:
                return (C, pos, relpos, Output, True)
            else:
                a = Input.pop(0)
                write(a, pos+1, ma)
                step = 2
                
        elif oc == 4:
            Output.append(read(pos+1, ma))
            step=2
            
        elif oc == 5:
            a = read(pos+1, ma)
            b = read(pos+2, mb)
            if a != 0:
                pos = b
                step = 0
            else:
                step = 3
                
        elif oc == 6:
            a = read(pos+1, ma)
            b = read(pos+2, mb)
            if a == 0:
                pos = b
                step = 0
            else:
                step = 3
                
        elif oc == 7:
            a = read(pos+1, ma)
            b = read(pos+2, mb)
            write(int(a < b), pos+3, mc)
            step = 4
            
        elif oc == 8:
            a = read(pos+1, ma)
            b = read(pos+2, mb)
            write(int(a == b), pos+3, mc)
            step = 4
            
        elif oc == 9:
            a = read(pos+1, ma)
            relpos += a
            step = 2
            
        pos += step


# Part 1
beamdata = []
for y in range(50):
    for x in range(50):
        C = copy.deepcopy(CODE)
        (C, pos, relpos, Output, running) = intcom(C, 0, 0, [x,y], True)
        beamdata = beamdata + Output
print(sum(beamdata))

# Part 2
rightedge = 616
for y in range(1001,2000):
    C = copy.deepcopy(CODE)
    (C, pos, relpos, Output, running) = intcom(C, 0, 0, [rightedge+1,y], True)
    rightedge += Output[0]
    C = copy.deepcopy(CODE)
    (C, pos, relpos, Output, running) = intcom(C, 0, 0, [rightedge-99,y+99], True)
    if Output[0]:
        print((rightedge-99)*10000+y)
        break



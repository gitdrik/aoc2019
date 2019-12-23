import copy

CODE = [];
with open('23.txt') as f:
    nums = f.read().strip().split(',')
    for n in nums:
        CODE.append(int(n))
            
# Extend memmory "alot"
CODE += [0]*3*len(CODE)

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
            pos += 4
            
        elif oc == 2:
            a = read(pos+1, ma)
            b = read(pos+2, mb)
            write(a * b, pos+3, mc)
            pos += 4
            
        elif oc == 3:
            if Input == []:
                return (C, pos, relpos, Output, True)
            else:
                a = Input.pop(0)
                write(a, pos+1, ma)
                pos += 2
                
        elif oc == 4:
            Output.append(read(pos+1, ma))
            pos +=2
            
        elif oc == 5:
            a = read(pos+1, ma)
            b = read(pos+2, mb)
            if a != 0:
                pos = b
            else:
                pos += 3
                
        elif oc == 6:
            a = read(pos+1, ma)
            b = read(pos+2, mb)
            if a == 0:
                pos = b
            else:
                pos += 3
                
        elif oc == 7:
            a = read(pos+1, ma)
            b = read(pos+2, mb)
            write(int(a < b), pos+3, mc)
            pos += 4
            
        elif oc == 8:
            a = read(pos+1, ma)
            b = read(pos+2, mb)
            write(int(a == b), pos+3, mc)
            pos += 4
            
        elif oc == 9:
            a = read(pos+1, ma)
            relpos += a
            pos += 2


def shipnet():
    # Number of NICS
    n = 50

    # Make nics
    NICS = []
    for i in range(n):
        NICS.append([copy.deepcopy(CODE), 0, 0, [i], True])

    # The nat
    NAT = [0,0]
    NATy = set()
    idelc = 0


    partone = True
    parttwo = True

    i = 0
    while 1:
        
        idle = True
        
        # run a NIC
        if NICS[i][3] == []:
            NICS[i][3] = [-1]
        else:
            idle = False
            
        (NICS[i][0],NICS[i][1],NICS[i][2], Output, NICS[i][4]) = (
            intcom(NICS[i][0],NICS[i][1],NICS[i][2],NICS[i][3],NICS[i][4]))

        # Take care of Output
        for j in range(0,len(Output),3):
            idle = False
            if Output[j] in range(n):
                NICS[Output[j]][3] += copy.deepcopy(Output[j+1:j+3])
            elif Output[j] == 255:
                NAT = Output[j+1:j+3]
                if partone:
                    partone = False
                    print('Part 1: ',NAT[1])
                
                #print(NAT)
            else:
                print('Packet sent to to /DEV/NULL')
                
        if idle:
            idelc += 1
        else:
            idelc = 0

        if idelc == 50:
            idelc = 0
            NICS[0][3] += NAT
            if parttwo:
                if NAT[1] in NATy:
                    print('Part 2: ',NAT[1])
                    parttwo = False
                else:
                    NATy.add(NAT[1])
                
        i = (i+1) % n
            
            
shipnet()

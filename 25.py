CODE = [];
with open('25.txt') as f:
    nums = f.read().strip().split(',')
    for n in nums:
        CODE.append(int(n))
            
# Extend memmory "alot"
CODE += [0]*5*len(CODE)

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
                #return (C, pos, relpos, Output, True)
                Input = [ord(x) for x in (input()+'\n')]
            else:
                a = Input.pop(0)
                write(a, pos+1, ma)
                pos += 2
                
        elif oc == 4:
            #Output.append(read(pos+1, ma))
            print(chr(read(pos+1, ma)),end='')
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

intcom(CODE,0,0,[],True)

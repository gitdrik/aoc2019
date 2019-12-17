CODE = [];
with open('17.txt') as f:
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


def partone():
    global CODE
    (CODE, pos, relpos, Output, running) = intcom(CODE, 0, 0, [], True)
    os = ''.join(map(chr, Output))
    print(os)
    ol = os.strip().split('\n')
    cs = 0
    for i in range(1,len(ol)-1):
        for j in range(1,len(ol[0])-1):
            if ((ol[i][j] ==  '#') and
                (ol[i-1][j] ==  '#') and
                (ol[i+1][j] ==  '#') and
                (ol[i][j-1] ==  '#') and
                (ol[i][j+1] ==  '#')):
                cs += i*j
    print(cs)

def parttwo():
    global CODE
    CODE[0] = 2
    pos = 0
    relpos = 0
    inMain = 'A,B,A,B,C,A,B,C,A,C\n'
    inA = 'R,6,L,10,R,8\n'
    inB = 'R,8,R,12,L,8,L,8\n'
    inC = 'L,10,R,6,R,6,L,8\n'
    inF = 'n\n'
    In =[ord(x) for x in inMain + inA + inB + inC + inF]
    (CODE, pos, relpos, Output, running) = intcom(CODE, pos, relpos, In, True)
    os = ''.join(map(chr, Output[:-2]))
    print(Output[-1])

#partone()
parttwo()

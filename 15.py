CODE = [];
with open('repairdroid.txt') as f:
    for line in f:
        line = line.strip()
        nums = line.split(',')
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
            
        pos += step


def mapmaker(steps, dirs, rpos, MAP, STEPS, CODE, pos, relpos, running):
    for dir in dirs:
        if dir == 1:
            newpos = [rpos[0]-1, rpos[1]]
            newdirs = [1,3,4]
        elif dir == 2:
            newpos = [rpos[0]+1, rpos[1]]
            newdirs = [2,3,4]
        elif dir == 3:
            newpos = [rpos[0], rpos[1]-1]
            newdirs = [1,2,3]
        elif dir == 4:
            newpos = [rpos[0], rpos[1]+1]
            newdirs = [1,2,4]
            
        if (MAP[newpos[0]][newpos[1]] == 0) or (steps+1 >= STEPS[newpos[0]][newpos[1]]):
            # no reason to try
            continue
        else:
            # try to make the step
            (CODE, pos, relpos, Output, running) = intcom(CODE, pos, relpos, [dir], running)
            if Output[-1] == 0:
                # Hit an unknown wall
                MAP[newpos[0]][newpos[1]] = 0
            elif (Output[-1] == 1) or (Output[-1] == 2):
                # Sucess, robot moved, make map
                MAP[newpos[0]][newpos[1]] = Output[-1]
                STEPS[newpos[0]][newpos[1]] = steps + 1
                # make maps from newpos                
                (MAP, STEPS, CODE, pos, relpos, running) = mapmaker(
                    steps+1, newdirs, newpos, MAP, STEPS, CODE, pos, relpos, running)
                # move back to current position
                reverse = (dir == 1)*2 + (dir == 2)*1 + (dir == 3)*4 + (dir == 4)*3
                (CODE, pos, relpos, Output, running) = intcom(CODE, pos, relpos, [reverse], running)
    return (MAP, STEPS, CODE, pos, relpos, running)
                

# Empty map
# 0: wall, 1:floor, 2:oxygen; north (1), south (2), west (3), and east (4)
size = 42
MAP = [[1]*size for _ in range(size)]
STEPS = [[size*size]*size for _ in range(size)]
rpos = [size//2,size//2]
dirs = [1,2,3,4]
MAP[rpos[0]][rpos[1]] = 1
MAP[rpos[0]][rpos[1]] = 0

# initialize intcom
pos = 0
relpos=0
running = True

# Make maps
(MAP, STEPS, CODE, pos, relpos, running) = mapmaker(0, dirs, rpos, MAP, STEPS, CODE, pos, relpos, running)

# Part 1
for i in range(len(MAP)):
    for j in range(len(MAP[i])):
        if MAP[i][j] == 2:
            print(STEPS[i][j])

# Part 2
def goto2o(steps, dirs, rpos, MAP, STEPS, CODE, pos, relpos, running):
    found = False
    if MAP[rpos[0]][rpos[1]] != 2:
        for dir in dirs:
            if dir == 1:
                newpos = [rpos[0]-1, rpos[1]]
                newdirs = [1,3,4]
            elif dir == 2:
                newpos = [rpos[0]+1, rpos[1]]
                newdirs = [2,3,4]
            elif dir == 3:
                newpos = [rpos[0], rpos[1]-1]
                newdirs = [1,2,3]
            elif dir == 4:
                newpos = [rpos[0], rpos[1]+1]
                newdirs = [1,2,4]
            
            if (MAP[newpos[0]][newpos[1]] == 0) or (steps+1 > STEPS[newpos[0]][newpos[1]]):
                continue
            else:
                # make the step
                (CODE, pos, relpos, Output, running) = intcom(CODE, pos, relpos, [dir], running)
                # search from new pos              
                (newrpos, found, CODE, pos, relpos, running) = goto2o(
                        steps+1, newdirs, newpos, MAP, STEPS, CODE, pos, relpos, running)
                if not(found):
                    # move back to current position
                    reverse = (dir == 1)*2 + (dir == 2)*1 + (dir == 3)*4 + (dir == 4)*3
                    (CODE, pos, relpos, Output, running) = intcom(CODE, pos, relpos, [reverse], running)
                else:
                    rpos = newrpos
                    break
    else:
        found = True
            
    return (rpos, found, CODE, pos, relpos, running)

# Go to oxygen
(rpos, found, CODE, pos, relpos, running) = goto2o(0, dirs, rpos, MAP, STEPS, CODE, pos, relpos, running)
# Calculate minutes
MINS = [[size*size]*size for _ in range(size)]
(MAP, MINS, CODE, pos, relpos, running) = mapmaker(0, dirs, rpos, MAP, MINS, CODE, pos, relpos, running)

maxmins = 0
for i in range(len(MINS)):
    for j in range(len(MINS[i])):
        if MINS[i][j] != size*size:
            maxmins = max(maxmins,MINS[i][j])
            
print(maxmins)

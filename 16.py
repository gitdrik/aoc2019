with open('16.txt') as f:
    signal = f.read().strip()

pattern = [0,1,0,-1]
plength = len(pattern)
out = ''

for p in range(100):
    for i in range(len(signal)):
        digit = 0
        for j in range(len(signal)):
            multiplier = pattern[(j+1)//(i+1) % plength]
            digit += int(signal[j])*multiplier
        out += str(abs(digit) % 10)
    signal = out
    out = ''

print(signal[:8])

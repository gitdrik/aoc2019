# pixels
pixels = []
with open('input8.txt') as f:
    for line in f:
        for i in line:
            pixels.append(int(i))
# rows
rows = []
width = 25
for i in range(0, len(pixels), width):
    rows = rows + [pixels[i:(i+width)]]
    
# layers
layers = []
height = 6
for i in range(0, len(rows), height):
    layers = layers + [rows[i:(i+height)]]

######### first part
zerosPerLayer = list(map(lambda x:x.count(0),
                          list(map(lambda x:sum(x,[]),layers))))

minLayer = zerosPerLayer.index(min(zerosPerLayer))

print( sum(map(lambda x:x.count(1),layers[minLayer])) *
       sum(map(lambda x:x.count(2),layers[minLayer])), end='\n\n')

######### second part
for row in range(height):
    for column in range(width):
        for layer in range(100):
            pixel = layers[layer][row][column]
            if pixel!=2:
                if pixel == 1:
                    print('O',end='')
                else:
                    print(' ',end='')
                break
    print('')

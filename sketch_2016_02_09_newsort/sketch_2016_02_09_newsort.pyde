filename = 'sandman.jpg'
blockFactor = 10
mirrorFactor = 2

def setup():
    size(500, 349)
    img = loadImage(filename)
    image(img,0, 0)

def draw():
    global blockFactor, mirrorFactor
    loadPixels()
    sortPixels()
    updatePixels()
    saveFrame('output/###.png')
    if frameCount >= 1:
        exit()

def sortPixels():
    pixMat = []
    i = 0
    l = 1
    while i <= len(pixels)-width:
        tempMat = []
        blocks = int(width/blockFactor)
        for j in range (i, i+blocks+1):
            tempMat.append(pixels [j])
        tempMat.sort()
        #blockFactor = random(1, 50)
        if l % mirrorFactor == 0:
            tempMat.reverse()
        else:
            pass
        for k in range (0, len(tempMat)-1):
            pixMat.append(tempMat [k])
        i += (width)/blockFactor
        l += 1
        if i % width == 0:
            i += 1
        else:
            pass
    #print len(pixMat)
    del pixels [:]
    for i in range (0, len(pixMat)-1):
        pixels.append(pixMat [i])
    
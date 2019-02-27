filename = 'try1.png'
blockFactor = 2
mirrorFactor = 5000

# VALUES

blackValue = -1000000

def setup():
    size(1280, 1280)
    img = loadImage(filename)
    image(img, 0, 0)

def draw():
    global blockFactor, mirrorFactor, blackValue
    loadPixels()
    sortPixels()
    updatePixels()
    saveFrame('output/###.png')
    if frameCount >= 1:
        exit()

def sortPixels():
    pixMat = []
    for i in range (0, width*height-1):
        pixMat.append(pixels [i])
    i = 0
    l = 1
    blockLength = int(width/blockFactor)
    while i <= len(pixels)-blockLength:
        tempMat = []
        if i % width == 0:
            blockLength -= 1
        if brightness(pixMat[i]) > 150:
            i += 1
        elif saturation(pixMat[i]) > 250:
            i -= 3
            l += 1
        elif blue(pixMat[i]) > 150 and red(pixMat[i]) < 50:
            blockLength = int(blockLength*0.9)
        elif red(pixMat[i]) > 150 and green(pixMat[i]) < 50:
            i += 2
            blockLength += 2
        elif red(pixMat[i]) > 150 and green(pixMat[i]) > 150:
            i += 2
            blockLength = int(blockLength*1.5)
        else:
            i -= 100
        for j in range (i, i+blockLength-1):
            tempMat.append(pixMat [j])
        tempMat.sort()
        if l % mirrorFactor == 0:
            tempMat.reverse()
        for k in range (0, len(tempMat)-1):
            if len(tempMat) <= 0:
                break
            pixMat [i+k] = tempMat [k]
        i += blockLength
        l += 1
    for i in range (0, len(pixMat)-1):
        pixels [i] = pixMat [i]
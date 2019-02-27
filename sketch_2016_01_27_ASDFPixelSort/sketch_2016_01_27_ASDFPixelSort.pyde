sortMode = 0
# 0 = black
# 1 = bright
# 2 = white

imgFileName = "ISS019-E-014918_lrg.jpg"

sortLoops = 1
blackValue = -10000000
brightnessValue = 60
whiteValue = -6000000

column = 0
row = 0

def setup ():
    size (1440, 1080)
    global img
    img = loadImage (imgFileName)
    image (img, 0, 0)

def draw ():
    global sortMode, blackValue, brightnessValue, whiteValue
    sortMode = sortMode
    blackValue = blackValue
    brightnessValue = brightnessValue
    whiteValue = whiteValue
    loadPixels ()
    for column in range (width - 1):
        sortColumn (column, 0)
    updatePixels ()
    loadPixels ()
    for row in range (height - 1):
        sortRow (0, row)
    updatePixels ()
    image (img, 0, 0)
    saved = 0
    if saved == 0 and frameCount >= sortLoops:
        saveFrame ("sort-###.png")
        saved = 1
        print 'OI FUK U M8'
        exit()

def sortColumn (x, y):
    yEnd = 0
    while yEnd < (height - 1):
        for a in (0, 0):
            if sortMode == 0:
                y = getFirstNotBlackY (x, y)
                yEnd = getNextBlackY (x, y)
                break
            elif sortMode == 1:
                y = getFirstBrightY (x, y)
                yEnd = getNextDarkY (x, y)
                break
            elif sortMode == 2:
                y = getFirstNotWhiteY (x, y)
                yEnd = getNextWhiteY (x, y)
                break
            else:
                break
        if y < 0:
            break
        sortLength = yEnd - y
        #print yEnd
        #print sortLength
        unsorted = [0 for x in range (sortLength)]
        for i in range (sortLength - 1):
            unsorted [i] = (pixels [x + (y + i) * width])
        sortedList = sorted(unsorted)
        #print sortedList
        for i in range (sortLength - 1):
            pixels[(x + (y + i) * width)] = sortedList[i]
        y = yEnd + 1

def sortRow (x, y):
    xEnd = 0
    while xEnd < (width - 1):
        for a in (0, 0):
            if sortMode == 0:
                x = getFirstNotBlackX (x, y)
                xEnd = getNextBlackX (x, y)
                break
            elif sortMode == 1:
                x = getFirstBrightX (x, y)
                xEnd = getNextDarkX (x, y)
                break
            elif sortMode == 2:
                x = getFirstNotWhiteX (x, y)
                xEnd = getNextWhiteX (x, y)
                break
            else:
                break
        if x < 0:
            break
        sortLength = xEnd - x
        unsorted = [0 for x in range (sortLength)]
        for i in range (sortLength - 1):
            unsorted.append (pixels [x + i + y * width])
        sortedList = sorted(unsorted)
        for i in range (sortLength - 1):
         pixels[(x + i + y * width)] = sortedList[i]
        x = xEnd + 1

# BLACK
def getFirstNotBlackX (x, y):
    c = pixels [x + y * width]
    while c < blackValue:
        x += 1
        if x >= width:
            return -1
    return x

def getNextBlackX (x, y):
    x = x + 1
    c = pixels [x + y * width]
    while c > blackValue:
        x += 1
        if x >= width:
            return (width - 1)
    return (x - 1)

def getFirstNotBlackY (x, y):
    c = pixels [x + y * width]
    while c < blackValue:
        y += 1
        if y >= height:
            return -1
    return y

def getNextBlackY (x, y):
    y = y + 1
    c = pixels [x + y * width]
    #print c
    if y < height:
        while c > blackValue:
            y += 1
            if y >= height:
                return (height - 1)
    return (y - 1)

# BRIGHTNESS
def getFirstBrightX (_x, _y):
    x = _x
    y = _y
    c = pixels[x + y * img.width]
    while brightness (c) < brightnessValue:
        x += 1
        if x >= img.width:
            return -1
    return x

def getNextDarkX (_x, _y):
    x = _x + 1
    y = _y
    c = pixels [x + y * img.width]
    while brightness (c) > brightnessValue:
        x += 1
        if x >= img.width:
            return (img.width - 1)
    return (x - 1)

def getFirstBrightY (_x, _y):
    x = _x
    y = _y
    c = pixels [x + y * img.width]
    while brightness (c) < brightnessValue:
        y += 1
        if y >= img.height:
            return -1
    return y

def getNextDarkY (_x, _y):
    x = _x
    y = _y + 1
    c = pixels [x + y * img.width]
    if y < img.height:
        while brightness (c) > brightnessValue:
            y += 1
            if y >= img.height:
                return (img.height - 1)
    return (y - 1)

# WHITE
def getFirstNotWhiteX (_x, _y):
    x = _x
    y = _y
    #c = pixels[x + y * img.width]
    while whiteValue < pixels [x + y * img.width]:
        x += 1
        if x >= img.width:
            return -1
    return x

def getNextWhiteX (_x, _y):
    x = _x + 1
    y = _y
    #print x
    if x < img.height:
        c = pixels [x + y * img.width]
        #print c
        while whiteValue > pixels [x + y * img.width]:
            #print x
            x += 1
            if x >= img.width:
                return (img.width - 1)
    return (x - 1)

def getFirstNotWhiteY (_x, _y):
    x = _x
    y = _y
    if y < img.height:
        #c = pixels [x + y * img.width]
        #print c
        while whiteValue < pixels [x + y * img.width]:
            #print pixels [x + y * img.width]
            y += 1
            if y >= img.height:
                return -1
    return y

def getNextWhiteY (_x, _y):
    x = _x
    y = _y + 1
    #print y
    if y < img.height:
        c = pixels [x + y * img.width]
        #print c
        while whiteValue > pixels [x + y * img.width]:
            #print y
            y += 1
            if y >= img.height:
                return (img.height - 1)
    return (y - 1)
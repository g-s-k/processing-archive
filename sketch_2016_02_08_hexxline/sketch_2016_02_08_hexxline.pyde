# INITIALIZE
loopLength = 25
nShapes = 2000
dim = 500
tick1 = 0
tick2 = 0

class hexx (object):
    def __init__(self, index):
        self.index = index
        self.xpos = -2 * dim + self.index * 5 * dim / nShapes
        #self.ypos = -2 * dim + self.index * 5 * dim / nShapes
        #self.xpos = int(random(-2 * dim, 3 * dim))
        self.ypos = int(random(-2 * dim, 3 * dim))
        self.zpos = random(- dim * 5, dim)
        self.zSpeed = dim * 2 / loopLength
        self.rad = 10
        self.rotFactor = (-1) ** int(random(2))
    def display(self):
        translate(self.xpos, self.ypos, self.zpos)
        rotateZ(tick1 / 6 * self.rotFactor)
        drawCylinder(6, self.rad, 5)
    def move(self):
        self.zSpeed = self.zSpeed #+ 5 * mod1
        self.zpos = self.zpos + self.zSpeed
        if self.zpos >= dim:
            self.zpos = - dim * 5

def setup():
    size(dim, dim, OPENGL)
    frameRate(loopLength)

goodShitHexx = []
for i in range (0, nShapes):
    goodShitHexx.append(hexx (i)) 

def draw():
    global dim, loopLength, tick1, tick2, mod1
    tick1 += TWO_PI / loopLength
    tick2 += 255 / loopLength
    mod1 = sin(tick1)
    colorMode(HSB)
    background(tick2 % 255, 255, 40)
    stroke(0, 0, 150, 200)
    strokeWeight(2)
    fill((tick2 - 50) % 255, 150, 150, 75)
    for i in range (0, len(goodShitHexx)):
        goodShitHexx[i].move()
        with pushMatrix():
            goodShitHexx[i].display()
    saveFrame('frames/####.png')
    if frameCount >= loopLength * 3:
        exit()

def drawCylinder (nsides, radius, h):
    angle = TWO_PI / nsides
    halfHeight = h / 2
    with beginShape ():
        for i in range (0, nsides):
            x = cos (i * angle) * radius
            y = sin (i * angle) * radius
            vertex (x, y, -halfHeight)
    with beginShape ():
        for i in range (0, nsides):
            x = cos (i * angle) * radius
            y = sin (i * angle) * radius
            vertex (x, y, halfHeight)
    with beginShape (QUAD_STRIP):
        for i in range (0, (nsides + 1)):
            x = cos(i * angle ) * radius
            y = sin(i * angle ) * radius
            vertex ( x, y, halfHeight)
            vertex ( x, y, -halfHeight)
    
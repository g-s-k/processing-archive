counter1 = 0
loopLength = 75

class cylinder (object):
    def __init__ (self, index, nSides, rotationDir, radInit, heightInit, hueInit, strokeValue, alphaRate, radiusA, radiusC, heightA, heightB):
        self.index = index
        self.strokeValue = strokeValue
        self.hueInit = random (hueInit, hueInit + 25)
        self.satInit = random (60, 90)
        self.brightInit = random (50, 95)
        self.alphaInit = random (5, 25)
        self.alphaRate = alphaRate
        self.xpos = random (200, 880)
        self.ypos = random (200, 880)
        self.zpos = random (-600, -400)
        self.rDir = rotationDir
        self.pulseEffect = random (-100, 100)
        self.n = nSides
        self.radius = random (radInit, radInit + 150)
        self.h = random (heightInit, heightInit * 2)
        self.radiusA = radiusA
        self.radiusC = radiusC
        self.heightA = heightA
        self.heightB = heightB
    def display (self):
        fill (colorSweep (self.hueInit, self.satInit, self.brightInit, self.alphaInit, counter2, mod1, 0, (mod3 * self.alphaRate)))
        stroke (0, 0, self.strokeValue, (self.alphaInit - 40 + 20 * mod1))
        shininess (random (1, 5))
        with pushMatrix ():
            translate ((self.xpos + self.pulseEffect * mod1), (self.ypos - self.pulseEffect * mod1), (self.zpos + 0.25 * abs (self.pulseEffect) * mod4))
            rotateX (counter2 % TWO_PI)
            rotateY (counter1 % TWO_PI)
            rotateZ ((self.rDir * counter2) % TWO_PI)
            drawCylinder (self.n, (self.radius - 125 * mod2 * self.radiusA - 50 * mod1 * self.radiusC), (self.h + (75 * mod2 * self.heightA) + (25 * mod3 * self.heightB)))

class mover (object):
    def __init__ (self):
        self.hueInit = random (100)
        self.satInit = random (60, 90)
        self.brightInit = random (10, 30)
        self.alphaInit = random (10, 25)
        self.xpos = random (-500, 1580)
        self.ypos = random (-500, 1580)
        self.zpos = random (-750, -600)
        self.xspeed = random (-1, 1)
        self.yspeed = random (-1, 1)
        self.zspeed = random (-1, 1)
        self.pulseEffect = random (-100, 100)
        self.n = 4
        self.radius = random (10, 30)

class moverCube (mover):
    def __init__ (self, index):
        mover.__init__ (self)
        self.index = index
    def display (self):
        fill (colorSweep (self.hueInit, self.satInit, self.brightInit, self.alphaInit, counter1, mod1, 0, 0))
        stroke (0, 0, 100, (self.alphaInit - 65 - 5 * mod2))
        shininess (random (5, 10))
        with pushMatrix ():
            translate ((self.xpos + 100 * self.xspeed * mod1), (self.ypos + 100 * self.yspeed * mod1), (self.zpos + 2 * abs (self.pulseEffect) * mod4))
            rotateX (counter2)
            rotateY (counter1)
            rotateZ (-counter3)
            box (self.radius)
            
class moverSphere (mover):
    def __init__ (self, index):
        mover.__init__ (self)
        self.index = index
    def display (self):
        fill (colorSweep (self.hueInit, self.satInit, self.brightInit, self.alphaInit, counter1, mod1, 0, 0))
        stroke (0, 0, 100, (self.alphaInit - 65 - 5 * mod2))
        shininess (random (5, 10))
        with pushMatrix ():
            translate ((self.xpos + 100 * self.xspeed * mod1), (self.ypos + 100 * self.yspeed * mod1), (self.zpos + 2 * abs (self.pulseEffect) * mod4))
            rotateX (counter2)
            rotateY (counter1)
            rotateZ (-counter3)
            sphereDetail (int (self.index * 0.01))
            sphere (self.radius)

def setup ():
    size (1080, 1080, OPENGL)
    colorMode (HSB, 100)

goodshitTri = []
for i in range (0,500):
    goodshitTri.append (cylinder (i, 3, -1, 75, 50, 50, 100, 1, 1, 0, 1, 0))
    
goodshitHex = []
for i in range (0,500):
    goodshitHex.append (cylinder (i, 6, 1, 75, 50, 40, 100, -0.5, 1, 0, 1, 0))
    
goodshitSqr = []
for i in range(0,500):
    goodshitSqr.append (cylinder (i, 4, -1, 50, 50, 60, 0, 1, 0, 1, 0, 1))
    
goodshitD = []
for i in range (0,500):
    goodshitD.append (moverCube (i))
    
goodshitE = []
for i in range (0,500):
    goodshitE.append (moverSphere (i))

def draw ():
    background (82.2, 58.6, 5.7)
    #background (54.4, 5, 95)
    global counter1, counter2, counter3
    counter1 = counter1 + TWO_PI / loopLength
    counter2 = counter1 * 5
    counter3 = counter1 * 20
    global mod1, mod2, mod3, mod4
    mod1 = sin (counter1)
    mod2 = sin (counter2)
    mod3 = sin (counter3)
    mod4 = cos (counter1)
    strokeWeight (1)
    #lights ()
    ambientLight (53.3, 75, 20)
    directionalLight (56.1, 76.7, 45.5, -1, -1, -0.25)
    directionalLight (44.7, 86.6, 10, -1, 1, -0.5)
    directionalLight (10, 75.6, 10, 1, 0, 0.25)
    spotLight (0, 0, 100, 0, 0, -750, 0, 0, 1, PI, 1)
    for i in range(0,len (goodshitTri)):
        with pushMatrix():
            goodshitTri[i].display()
    for i in range(0,len (goodshitHex)):
        with pushMatrix():
            goodshitHex[i].display()
    for i in range(0,len (goodshitSqr)):
        with pushMatrix():
            goodshitSqr[i].display()
    for i in range(0,len (goodshitD)):
        with pushMatrix():
            goodshitD[i].display()
    for i in range(0,len (goodshitD)):
        with pushMatrix():
            goodshitE[i].display()
    saveFrame("frames/####.png")
    if frameCount >= loopLength:
        exit ()

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
            
def colorSweep (hueInit, satInit, brightInit, alphaInit, hueRate, satRate, brightRate, alphaRate):
    hue1 = (hueInit + hueRate * 100 / TWO_PI) % 100
    sat1 = satInit + satRate * 25
    bright1 = brightInit + brightRate * 25
    alpha1 = alphaInit + alphaRate * 5
    fillColor = color (hue1, sat1, bright1, alpha1)
    return fillColor
# ENVIRONMENT PROPERTIES
windowSize = 750
loopLength = 450
captureLength = 450
redShiftMax = 5

# OBJECT PROPERTIES
nDots = 300
dotRad = 5
nIcos = 30
icoRad = 25
speed = 0.5

# CLASS DEFINITIONS
class Icosahedron(object):
    def __init__(self, index, radius=150):
        self.index = index
        self.h = TWO_PI * self.index / nIcos
        self.theta = TWO_PI * self.index / (nIcos + 1)
        self.phi = random(PI)
        self.rad = windowSize * 0.3
        self.position = PVector (self.rad * sin(self.phi) * cos(self.theta),
                                 self.rad * sin(self.phi) * sin(self.theta),
                                 self.rad * cos(self.phi))
        self.velocity = PVector (random(-speed, speed)*2,
                                 random(-speed, speed)*2,
                                 random(-speed, speed)*2)
        self.topPent = [PVector() for _ in range(5)]
        self.bottomPent = [PVector() for _ in range(5)]
        c = dist(cos(0) * radius,
                 sin(0) * radius,
                 cos(radians(72)) * radius,
                 sin(radians(72)) * radius)
        b = radius
        a = sqrt((c**2) - (b**2))
        self.triHeight = sqrt((c**2) - (c / 2)**2)
        angle = 0
        for i in range(5):
            self.topPent[i] = PVector(cos(angle) * radius,
                                      sin(angle) * radius,
                                      self.triHeight / 2.0)
            angle += radians(72)
        self.topPoint = PVector(0, 0, self.triHeight / 2.0 + a)
        angle = 72.0 / 2.0
        for i in range(5):
            self.bottomPent[i] = PVector(cos(angle) * radius,
                                         sin(angle) * radius,
                                         -self.triHeight / 2.0)
            angle += radians(72)
        self.bottomPoint = PVector(0, 0, -(self.triHeight / 2.0 + a))

    # Draw icosahedron.
    def create(self):
        for i in range(5):
            if i < 4:
                # Icosahedron top.
                self.makeTriangle(self.topPent[i],
                                  self.topPoint,
                                  self.topPent[i + 1])
                # Icosahedron bottom.
                self.makeTriangle(self.bottomPent[i],
                                  self.bottomPoint,
                                  self.bottomPent[i + 1])
            else:
                self.makeTriangle(self.topPent[i],
                                  self.topPoint,
                                  self.topPent[0])
                self.makeTriangle(self.bottomPent[i],
                                  self.bottomPoint,
                                  self.bottomPent[0])

        # Icosahedron body.
        for i in range(5):
            if i < 3:
                self.makeTriangle(self.topPent[i],
                                  self.bottomPent[i + 1],
                                  self.bottomPent[i + 2])
                self.makeTriangle(self.bottomPent[i + 2],
                                  self.topPent[i],
                                  self.topPent[i + 1])
            elif i == 3:
                self.makeTriangle(self.topPent[i],
                                  self.bottomPent[i + 1],
                                  self.bottomPent[0])
                self.makeTriangle(self.bottomPent[0],
                                  self.topPent[i],
                                  self.topPent[i + 1])
            elif i == 4:
                self.makeTriangle(self.topPent[i],
                                  self.bottomPent[0],
                                  self.bottomPent[1])
                self.makeTriangle(self.bottomPent[1],
                                  self.topPent[i],
                                  self.topPent[0])

    def makeTriangle(self, a, b, c):
        with beginShape():
            vertex(a.x, a.y, a.z)
            vertex(b.x, b.y, b.z)
            vertex(c.x, c.y, c.z)
    
    def make(self):
        # APPEARANCE
        colorMode(HSB, TWO_PI)
        fill((self.h + tick1) % TWO_PI, TWO_PI, HALF_PI + HALF_PI * mod2)
        colorMode(RGB, 255)
        stroke(200, 125 - 125 * mod2)
        strokeWeight(1)
        
        #DRAW
        with pushMatrix():
            translate(self.position.x,
                      self.position.y,
                      self.position.z)
            rotateX(tick1)
            rotateY(tick1)
            rotateZ(tick1)
            self.create()
        
        # NORMAL MOTION
        self.position += self.velocity
        
        # WALL COLLISIONS
        self.loc = self.position / self.position.mag()
        if self.position.mag() >= windowSize / 3:
            self.position.setMag(windowSize / 3)
            self.velocity.sub(2 * self.velocity.dot(self.loc) * self.loc)
        
        # OBJECT COLLISIONS
        for i in range (len(goodShitB)):
            if i == self.index:
                break
            elif self.position.dist(goodShitB[i].position) <= icoRad:
                displacement = self.position - goodShitB[i].position
                displacement.normalize()
                self.velocity.sub(2 * self.velocity.dot(displacement) * displacement)
                goodShitB[i].velocity.sub(2 * goodShitB[i].velocity.dot(displacement) * displacement)
                del displacement

class dots (object):
    def __init__(self, index):
        self.index = index
        self.theta = random(TWO_PI)
        self.phi = PI * self.index / nDots
        self.rad = random(windowSize / 3, windowSize * 0.35)
        self.c = color(random(30, 250), random(30, 250), random(30, 250))
        self.position = PVector (self.rad * sin(self.phi) * cos(self.theta),
                                 self.rad * sin(self.phi) * sin(self.theta),
                                 self.rad * cos(self.phi))
        self.velocity = PVector (random(-speed, speed),
                                 random(-speed, speed),
                                 random(-speed, speed))

    def display(self):
        # APPEARANCE
        fill(self.c)
        noStroke()
        
        # DRAW
        with pushMatrix():
            translate(self.position.x,
                      self.position.y,
                      self.position.z)
            rotateX(tick2 * (-1) ** (self.index % 3))
            rotateY(tick1 * (-1) ** self.index)
            rotateZ(tick1 * (-1) ** (self.index % 4))
            sphereDetail(5 * self.index / nDots)
            sphere(dotRad)

    def move(self):
        # NORMAL MOTION
        self.position += self.velocity
        # WALL COLLISIONS
        self.loc = self.position.copy()
        self.loc.normalize()
        if self.position.mag() >= windowSize * 0.35:
            self.position.setMag(windowSize * 0.35)
            self.velocity.sub(2 * self.velocity.dot(self.loc) * self.loc)
        if self.position.mag() <= windowSize / 3:
            self.position.setMag(windowSize / 3)
            self.velocity.sub(2 * self.velocity.dot(self.loc) * self.loc)

class noiseThings (object):
    def __init__(self, index):
        self.index = index
        self.position = PVector (self.index % (windowSize * 3),
                                 int(self.index / (windowSize * 3)),
                                 0)
        noiseDetail(1, 0.5)
        self.c = color(noise(self.position.x * 0.01,
                             self.position.y * 0.01,
                             self.position.z * 0.01) * 255, 50)
    def display(self):
        stroke(self.c)
        strokeWeight(1)
        point(self.position.x - windowSize,
              self.position.y - windowSize,
              self.position.z)

# PROCESSING RUNTIME
def setup():
    size(windowSize, windowSize, OPENGL)
    global goodShitA, goodShitB, goodShitC, tick1
    tick1 = 0
    goodShitA = [dots(i) for i in range (nDots)]
    goodShitB = [Icosahedron(j, icoRad) for j in range (nIcos)]
    #goodShitC = [noiseThings(k) for k in range ((windowSize * 2) ** 2)]

def draw():
    # ENVIRONMENT
    background(20)
    lights()
    
    # MODULATION
    global tick1, tick2, mod1, mod2
    tick1 += TWO_PI / loopLength
    tick2 = tick1 * 2
    mod1 = sin(tick1)
    mod2 = sin(tick2)

    
    # CAMERA POSITION AND MOTION
    with beginCamera():
        camera()
        translate(windowSize/2, windowSize/2, 0)
        rotateX(tick1/3)
        rotateY(tick1/2)
        rotateZ(tick1)
    
    # DRAW
    for i in range (len(goodShitA)):
        goodShitA[i].display()
        goodShitA[i].move()
    for j in range (len(goodShitB)):
        goodShitB[j].make()
    #for k in range (len(goodShitC)):
        #goodShitC[k].display()
    
    # CHANNEL SHIFT
    global redShift
    redShift = int(mod1 * redShiftMax)
    loadPixels()
    for i in range (len(pixels) - redShiftMax):
        pixels[i] = color(red(pixels[i + redShift]),
                          green(pixels[i]),
                          blue(pixels[i]))
    updatePixels()
    
    # SAVE & EXIT
    saveFrame('frames/####.png')
    if frameCount >= captureLength:
        exit()
        pass
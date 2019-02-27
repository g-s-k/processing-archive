# GENERAL
loopLength = 70
     
class Icosahedron(object):
    def __init__(self, radius=150, x=0, y=0, z=0):
        self.locationX = x
        self.locationY = y
        self.locationZ = z
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

class fallCube(object):
    def __init__(self, index):
        self.index = index
        self.radius = 25
        self.c = random(255)
        self.rotFactorA = (-1) ** int(random(2.1))
        self.rotFactorB = (-1) ** int(random(2.1))
        self.pos = PVector (random(-150, 650),
                            random(-150, 650),
                            -250)

    def display(self):
        with pushMatrix():
            translate(self.pos.x, self.pos.y, self.pos.z)
            rotateX(tick1*self.rotFactorA)
            rotateY(tick1/2)
            rotateZ(tick1/4*self.rotFactorB)
            noFill()
            #fill(255, 50)
            colorMode(HSB)
            stroke((tick1*255/TWO_PI + self.c)%255, 150, 75)
            colorMode(RGB)
            box(self.radius)

    def move(self):
        self.pos.y = self.pos.y + 800 / loopLength
        if self.pos.y >= 650:
            self.pos.y = -150

def setup():
    size(500, 500, OPENGL)
    global tick1, ico1, goodShit
    tick1 = 0
    ico1 = Icosahedron(125)
    goodShit = []
    for i in range (255):
        goodShit.append(fallCube(i))

def draw():
    background(15)
    lights()
    global tick1, mod1, mod2
    tick1 += TWO_PI/loopLength
    mod1 = sin(tick1)
    mod2 = cos(tick1)
    strokeWeight(2)
    with pushMatrix():
        translate(width/2, height/2, 0)
        rotateX(tick1/2)
        rotateY(-tick1/4)
        rotateZ(tick1/4)
        stroke(255, 75-50*mod2)
        noFill()
        box(250)
    with pushMatrix():
        translate(width/2, height/2, 0)
        rotateX(tick1)
        rotateY(-tick1)
        rotateZ(tick1)
        stroke(255, 50*mod1)
        fill(12, 167, 119, 75+25*mod2)
        ico1.create()
    for i in range (len(goodShit)):
        goodShit[i].display()
        #goodShit[i].move()
        pass
    saveFrame('frames/####.png')
    if frameCount >= loopLength-1:
        exit()
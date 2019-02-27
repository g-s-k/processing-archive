loopRate = 100
minSpeed = PI
maxSpeed = TWO_PI
circleRad = 250
centerDepth = 0
nBlocks = 5000
elasticity = 5

#

mod1 = 0
frontDepth = centerDepth + circleRad
backDepth = centerDepth - circleRad

class molecule (object):

    def __init__(self, index):
        self.index = index
        self.xpos = 375
        self.ypos = 375
        self.zpos = random(backDepth, frontDepth)
        self.speedFactor = random(minSpeed, maxSpeed) * (-1) ** index
        self.speed = PVector (cos(self.speedFactor), sin(self.speedFactor), (sqrt(sq(cos(self.speedFactor)) + sq(cos(self.speedFactor)))))
        self.c = color(random(50, 250), random(50, 250), random(50, 250))
        self.rad = 10

    def display(self):
        fill(self.c)
        stroke(self.c)
        point(self.xpos, self.ypos, self.zpos)
        #translate(self.xpos, self.ypos, self.zpos)
        #box (self.rad)

    def move(self):
        self.pos = PVector ((self.xpos - width / 2), (self.ypos - height / 2) , (self.zpos - centerDepth))
        self.xpos = self.xpos + self.speed.x
        self.ypos = self.ypos + self.speed.y
        self.zpos = self.zpos + self.speed.z
        self.dotProduct = elasticity * self.speed.dot(self.pos) / sq(circleRad)
        self.distance = dist(self.xpos, self.ypos, self.zpos, width/2, height/2, centerDepth)
        if self.distance >= circleRad:
            #self.speed.x -= self.dotProduct * (self.pos.x)
            #self.speed.y -= self.dotProduct * (self.pos.y)
            #self.speed.z -= self.dotProduct * (self.pos.z)
            #self.xpos = width/2
            #self.ypos = height/2
            #self.zpos = centerDepth
            self.speed -= self.pos * self.dotProduct
        else:
            pass

def setup():
    size(750, 750, OPENGL)

goodshit = []
for i in range(nBlocks):
    goodshit.append(molecule(i))

def draw():
    background(25)
    global mod1, lfo1, minSpeed, maxSpeed, circleRad, centerDepth, frontDepth, backDepth, elasticity
    mod1 = mod1 + TWO_PI / loopRate
    lfo1 = sin(mod1)
    for i in range(len(goodshit)):
        goodshit[i].move()
        with pushMatrix():
            goodshit[i].display()
    #saveFrame('blip-####.png')
    if frameCount >= 900:
        exit()
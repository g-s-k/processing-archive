loopLength = 60
speed = 5
elasticity = 0.75
nDots = 50000

class dots (object):
    def __init__(self, index):
        self.index = index
        self.position = PVector (0, 0)
        self.speed = random(speed*0.975,speed*1.025)
        self.direction = random(TWO_PI)
        self.velocity = PVector (self.speed*cos(self.direction)*1.5,
                                 self.speed*sin(self.direction))
        self.velocity.rotate(QUARTER_PI*self.index/nDots*0.1)
        self.c = color(random(100,150))
    def display(self):
        stroke(self.c)
        point(self.position.x+500, self.position.y+500)
    def move(self):
        self.position.add(self.velocity)
        self.loc = self.position / int(self.position.mag())
        if tick <= loopLength:
            if tick % loopLength/10 ==0:
                self.velocity.rotate(PI*0.35*(-1)**(self.index))
                pass
            elif tick % loopLength/20 == 0:
                self.velocity.rotate(HALF_PI*0.75*(-1)**(self.index % 3))
                pass
            elif tick % loopLength/15 == 0:
                self.velocity.rotate(HALF_PI*1.5*(-1)**(self.index % 5))
                pass
            elif tick % loopLength/2 == 0:
                self.velocity.rotate(HALF_PI*0.37*(-1)**(self.index % 4))
                pass
            elif tick % loopLength/6 == 0:
                self.velocity.rotate(HALF_PI*0.59*(-1)**self.index)
                pass
        if self.position.mag() >= 450:
            self.position.setMag(450)
            self.velocity.sub(2*self.velocity.dot(self.loc)*self.loc)
        elif tick % (self.index+1) == 0:
            self.velocity.rotate(QUARTER_PI*(-1)**self.index)

def setup():
    size(1000, 1000)
    global goodShit, tick
    tick = 0
    goodShit = [dots(i) for i in range (nDots)]

def draw():
    background(30)
    strokeWeight(2)
    global tick
    tick = tick + 1
    for i in range (len(goodShit)):
        goodShit[i].display()
        goodShit[i].move()
    saveFrame('frames/#####.png')
    if frameCount >= 6000:
        exit()
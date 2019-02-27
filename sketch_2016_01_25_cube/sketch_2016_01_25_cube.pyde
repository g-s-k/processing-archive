depth = 1000
min_speed = 1
max_speed = 4
elastic_min = 1
elastic_max = 1

class thingy (object):
    def __init__(self,index):
        self.index = index
        self.c1 = random (0,250)
        self.c2 = random (0,250)
        self.c3 = random (0,250)
        self.c = color (self.c1,self.c2,self.c3)
        self.s = color ((self.c1 * 0.5),(self.c2 * 0.5),(self.c3 * 0.5))
        self.rad = 25
        self.xpos = random (50,700)
        self.ypos = random (50,700)
        self.zpos = random ((-1 * depth), -10)
        self.xspeed = random (min_speed, max_speed) * (-1 ** random(2))
        self.yspeed = random (min_speed, max_speed) * (-1 ** random(2))
        self.zspeed = random (min_speed, max_speed) * (-1 ** random(2))
        self.rot = 0
        self.rotmult = random(1,3) * (-1 ** random(2))
    def display (self):
        fill (self.c)
        strokeWeight (2)
        stroke (self.s)
        translate (self.xpos, self.ypos, self.zpos)
        self.rot += 0.01 * self.rotmult
        rotateX (self.rot)
        rotateY (self.rot)
        rotateZ (self.rot)       
        box (2 * self.rad)
    def drive (self):
        global goodshit
        self.xpos =  self.xpos + self.xspeed
        if self.xpos > width - (self.rad * 1.75):
            self.xspeed = - self.xspeed
        if self.xpos < 0 + (self.rad * 1.75):
            self.xspeed = - self.xspeed
        self.ypos =  self.ypos + self.yspeed
        if self.ypos > height - (self.rad * 1.75):
            self.yspeed = - self.yspeed
        if self.ypos < 0 + (self.rad * 1.75):
            self.yspeed = - self.yspeed
        self.zpos = self.zpos + self.zspeed
        if self.zpos > 10:
            self.zspeed = - self.zspeed
        if self.zpos < (-1 * depth):
            self.zspeed = - self.zspeed
        for x in goodshit:
            if (sqrt((x.xpos - self.xpos)**2 + (x.ypos - self.ypos)**2 + (x.zpos - self.zpos)**2) < (self.rad * 2)) and (self.index != x.index):
                self.xspeed = - self.xspeed * random (elastic_min, elastic_max)
                self.yspeed = - self.yspeed * random (elastic_min, elastic_max)
                self.zspeed = - self.zspeed * random (elastic_min, elastic_max)
                break
        for x in goodshit2:
            if sqrt((x.xpos - self.xpos)**2 + (x.ypos - self.ypos)**2 + (x.zpos - self.zpos)**2) < (self.rad * 2):
                self.xspeed = - self.xspeed * random (elastic_min, elastic_max)
                self.yspeed = - self.yspeed * random (elastic_min, elastic_max)
                self.zspeed = - self.zspeed * random (elastic_min, elastic_max)
                break


class otherthingy (object):
    def __init__(self,index):
        self.index = index
        self.c1 = random (0,250)
        self.c2 = random (0,250)
        self.c3 = random (0,250)
        self.c = color (self.c1,self.c2,self.c3)
        self.s = color ((self.c1 * 0.5),(self.c2 * 0.5),(self.c3 * 0.5))
        self.rad = 25
        self.xpos = random (50,700)
        self.ypos = random (50,700)
        self.zpos = random ((-1 * depth), -10)
        self.xspeed = random (min_speed, max_speed) * (-1 ** random(2))
        self.yspeed = random (min_speed, max_speed) * (-1 ** random(2))
        self.zspeed = random (min_speed, max_speed) * (-1 ** random(2))
        self.rot = 0
        self.rotmult = random(1,3) * (-1 ** random(2))
    def display (self):
        fill (self.c)
        strokeWeight (2)
        stroke (self.s)
        translate (self.xpos, self.ypos, self.zpos)
        self.rot += 0.01 * self.rotmult
        rotateX (self.rot)
        rotateY (self.rot)
        rotateZ (self.rot)       
        sphereDetail (int (self.index / 30))
        sphere (self.rad)
    def drive (self):
        global goodshit
        self.xpos =  self.xpos + self.xspeed
        if self.xpos > width - (self.rad * 1.75):
            self.xspeed = - self.xspeed
        if self.xpos < 0 + (self.rad * 1.75):
            self.xspeed = - self.xspeed
        self.ypos =  self.ypos + self.yspeed
        if self.ypos > height - (self.rad * 1.75):
            self.yspeed = - self.yspeed
        if self.ypos < 0 + (self.rad * 1.75):
            self.yspeed = - self.yspeed
        self.zpos = self.zpos + self.zspeed
        if self.zpos > 10:
            self.zspeed = - self.zspeed
        if self.zpos < (-1 * depth):
            self.zspeed = - self.zspeed
        for x in goodshit:
            if sqrt((x.xpos - self.xpos)**2 + (x.ypos - self.ypos)**2 + (x.zpos - self.zpos)**2) < (self.rad * 2):
                self.xspeed = - self.xspeed * random (elastic_min, elastic_max)
                self.yspeed = - self.yspeed * random (elastic_min, elastic_max)
                self.zspeed = - self.zspeed * random (elastic_min, elastic_max)
                break
        for x in goodshit2:
            if (sqrt((x.xpos - self.xpos)**2 + (x.ypos - self.ypos)**2 + (x.zpos - self.zpos)**2) < (self.rad * 2)) and (self.index != x.index):
                self.xspeed = - self.xspeed * random (elastic_min, elastic_max)
                self.yspeed = - self.yspeed * random (elastic_min, elastic_max)
                self.zspeed = - self.zspeed * random (elastic_min, elastic_max)
                break

goodshit = []
for i in range(0,250):
    goodshit.append(thingy(i))
    
goodshit2 = []
for i in range(0,400):
    goodshit2.append(otherthingy(i))
    
def setup ():
    size (750,750, OPENGL)
    ambientLight (100, 100, 100)
    
def draw ():
    background (30)
    lights()
    for i in range(0,len(goodshit)):
        goodshit[i].drive()
        with pushMatrix():
            goodshit[i].display()
    for i in range(0,len(goodshit2)):
        goodshit2[i].drive()
        with pushMatrix():
            goodshit2[i].display()
        
    #saveFrame("cube-###.png")
class thingy (object):
    def __init__(self):
        self.c = color (200)
        self.s = color (100)
        self.rad = 12
        self.xpos = 500
        self.ypos = 500
        self.xspeed = 0
        self.yspeed = 0
    def display (self):
        fill (self.c)
        strokeWeight (2)
        stroke (self.s)
        ellipse (self.xpos, self.ypos, (2 * self.rad), (2 * self.rad))
    def drive (self):
        self.xpos =  self.xpos + self.xspeed
        if self.xpos > width + self.rad:
            self.xpos = 0
        if self.xpos < 0 - self.rad:
            self.xpos = width
        self.ypos =  self.ypos + self.yspeed
        if self.ypos > height + self.rad:
            self.ypos = 0
        if self.ypos < 0 - self.rad:
            self.ypos = height

thingy1 = thingy ()
thingy2 = thingy ()

def setup ():
    size (1000,1000)
    
def draw ():
    background (30)
    thingy1.drive ()
    thingy1.display ()
    thingy1.yspeed = (mouseY - 500) * 0.05
    thingy1.xspeed = (mouseX - 500) * 0.05
    thingy2.drive ()
    thingy2.display ()
    thingy2.c = color (141, 242, 194)
    thingy2.s = color (29, 78, 82)
    thingy2.yspeed = (mouseY - 500) * 0.1
    thingy2.xspeed = (mouseX - 500) * 0.1 * -1
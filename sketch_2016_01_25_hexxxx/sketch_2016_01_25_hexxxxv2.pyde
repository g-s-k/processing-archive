hexdim = 200
hexcolor = color (012, 167, 119)

class poly (object):
    def __init__ (self):
        self.xpos = 375 #random (250,500)
        self.ypos = 375 #random (250,500)
        self.rot = 0.01
    def display (self):
        strokeWeight (5)
        stroke (250,250,250)
        translate (self.xpos, self.ypos)
        rotate (HALF_PI)
        rotateX (self.rot)
        rotateY (-QUARTER_PI / 2)
        hexx (0, 0, hexdim)
        self.rot += 0.01

def setup ():
    size (750, 750, OPENGL)

hex1 = poly ()

def draw ():
    background (022, 006, 023)
    fill (hexcolor)
    with pushMatrix ():
        hex1.display ()
    

def hexx (x, y, radius):
    vMat = []
    with beginShape ():
        a1 = 0
        while a1 <=TWO_PI:
            sx = x + cos (a1) * radius
            sy = y + sin (a1) * radius
            fill (hexcolor)
            vertex (sx, sy, 0)
            a1 += PI / 3
        a2 = 0
        while a2 <=TWO_PI:
            sx = x + cos (a2) * radius
            sy = y + sin (a2) * radius
            fill (hexcolor)
            vertex (sx, sy, -100)
            vertex (sx, sy, 0)
            vertex (sx, sy, -100)
            a2 += PI / 3
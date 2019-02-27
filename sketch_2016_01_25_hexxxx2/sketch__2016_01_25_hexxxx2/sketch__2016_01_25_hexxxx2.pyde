import processing.opengl

hexdim = 200
hexcolor = color (012, 167, 119)

class poly (object):
    def __init__ (self):
        self.xpos = 375 #random (250,500)
        self.ypos = 375 #random (250,500)
        self.rot = 0.01
    def display (self):
        strokeWeight (5)
        stroke (225,225,225)
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
    hexFront = []
    hexBack = []
    angle = 0
    for i in range (0, 6):
        sx = x + cos (angle) * radius
        sy = y + sin (angle) * radius
        fill (hexcolor)
        hexFront.append (PVector (sx, sy, 0))
        hexBack.append (PVector (sx, sy, -100))
        angle += PI / 3
    for i in range (0, 6):
        with beginShape ():
            vertex (hexFront [i].x, hexFront [i].y, hexFront [i].z)
    for i in range (0, 6):
        with beginShape ():
            vertex (hexBack [i].x, hexBack [i].y, hexBack [i].z)
        if i < 5:
            for j in (0, 3):
                with beginShape ():
                    vertex (hexFront [i].x, hexFront [i].y, hexFront [i].z)
                    vertex (hexBack [i].x, hexBack [i].y, hexBack [i].z)
                    vertex (hexBack [i + 1].x, hexBack [i + 1].y, hexBack [i + 1].z)
                    vertex (hexFront [i + 1].x, hexFront [i + 1].y, hexFront [i + 1].z)
        else:
            for j in (0, 3):
                with beginShape ():
                    vertex (hexFront [i].x, hexFront [i].y, hexFront [i].z)
                    vertex (hexBack [i].x, hexBack [i].y, hexBack [i].z)
                    vertex (hexBack [0].x, hexBack [0].y, hexBack [0].z)
                    vertex (hexFront [0].x, hexFront [0].y, hexFront [0].z)
        
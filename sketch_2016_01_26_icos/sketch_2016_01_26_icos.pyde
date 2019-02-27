ico1 = Icosahedron ()

def setup ():
    size (750, 750, OPENGL)
    ico1 = Icosahedron (150)
    
def draw ():
    background (22,6,23)
    lights()
    translate (width/2, height/2)
    
    with pushMatrix ():
        rotateX (frameCount * PI / 175)
        rotateY (frameCount * PI / -200)
        stroke (104,12,65)
        fill (22,164,206)
        ico1.create ()

class Dimension3D (object):
    def __init__ (self, w, h, d):
        self._w = w
        self._h = h
        self._d = d


class Shape3D (object):
    def __init__ (self, w, h, d, x, y, z):
        self._w = w
        self._h = h
        self._d = d
        self._x = x
        self._y = y
        self._z = z
        self.v1 = PVector (self.x, self.y, self.z)

class Icosahedron (object):
    def __init__ (self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.topPent = []
        self.bottomPent = []
        self.angle = 0
        self.radius = 150
        self.c = dist (cos (0) * self.radius, sin (0) * self.radius, cos (radians (72)) * self.radius,  sin (radians (72)) * self.radius)
        self.b = radius
        self.a = sqrt ((c * c) - ((c / 2) * (c / 2)))
        self.triHt = sqrt ((c * c) - ((c / 2) * (c / 2)))
        for i in (0, 4):
            self.topPent.append = PVector (cos (angle) * radius, sin (angle) * radius, triHt / 2)
            angle += radians (72)
        self.topPoint = PVector (0, 0, (triHt / 2 + a))
        self.angle = self.angle / 2
        for i in (0, 4):
            self.bottomPent.append = PVector ((cos (angle) * radius), (sin (angle) * radius), (-triHt / 2))
            angle += radians (72)
        self.bottomPoint = PVector (0, 0, (-triHt / 2 + a))
    def create ():
        for i in (0, 4):
            # draw top tip
            with beginShape ():
                if i < 4:
                    vertex ((x + topPent [i].x), (y + topPent [i].y), (z + topPent [i].z))
                    vertex ((x + topPoint.x), (y + topPoint.y), (z + topPoint.z))
                    vertex ((x + topPent[i + 1].x), (y + topPent[i + 1].y), (z + topPent[i + 1].z))
                else:
                    vertex ((x + topPent[i].x), (y + topPent[i].y), (z + topPent[i].z))
                    vertex ((x + topPoint.x), (y + topPoint.y), (z + topPoint.z))
                    vertex ((x + topPent[0].x), (y + topPent[0].y), (z + topPent[0].z))
            # draw bottom tip
            with beginShape ():
                if i < 4:
                    vertex ((x + bottomPent [i].x), (y + bottomPent [i].y), (z + bottomPent [i].z))
                    vertex ((x + bottomPoint.x), (y + bottomPoint.y), (z + bottomPoint.z))
                    vertex ((x + bottomPent[i + 1].x), (y + bottomPent[i + 1].y), (z + bottomPent[i + 1].z))
                else:
                    vertex ((x + bottomPent[i].x), (y + bottomPent[i].y), (z + bottomPent[i].z))
                    vertex ((x + bottomPoint.x), (y + bottomPoint.y), (z + bottomPoint.z))
                    vertex ((x + bottomPent[0].x), (y + bottomPent[0].y), (z + bottomPent[0].z))
        # draw middle
        for i in (0, 4):
            if i < 3:
                with beginShape ():
                    vertex ((x + topPent [i].x), (y + topPent [i].y), (z + topPent [i].z))
                    vertex ((x + bottomPent[i + 1].x), (y + bottomPent[i + 1].y), (z + bottomPent[i + 1].z))
                    vertex ((x + bottomPent[i + 2].x), (y + bottomPent[i + 2].y), (z + bottomPent[i + 2].z))
                with beginShape ():
                    vertex ((x + bottomPent[i + 2].x), (y + bottomPent[i + 2].y), (z + bottomPent[i + 2].z))
                    vertex ((x + topPent [i].x), (y + topPent [i].y), (z + topPent [i].z))
                    vertex ((x + topPent[i + 1].x), (y + topPent[i + 1].y), (z + topPent[i + 1].z))
            elif i == 3:
                with beginShape ():
                    vertex ((x + topPent [i].x), (y + topPent [i].y), (z + topPent [i].z))
                    vertex ((x + bottomPent[i + 1].x), (y + bottomPent[i + 1].y), (z + bottomPent[i + 1].z))
                    vertex ((x + bottomPent[0].x), (y + bottomPent[0].y), (z + bottomPent[0].z))
                with beginShape ():
                    vertex ((x + bottomPent[0].x), (y + bottomPent[0].y), (z + bottomPent[0].z))
                    vertex ((x + topPent [i].x), (y + topPent [i].y), (z + topPent [i].z))
                    vertex ((x + topPent[i + 1].x), (y + topPent[i + 1].y), (z + topPent[i + 1].z))
            elif i == 4:
                with beginShape ():
                    vertex ((x + topPent [i].x), (y + topPent [i].y), (z + topPent [i].z))
                    vertex ((x + bottomPent[0].x), (y + bottomPent[0].y), (z + bottomPent[0].z))
                    vertex ((x + bottomPent[i + 2].x), (y + bottomPent[i + 2].y), (z + bottomPent[i + 2].z))
                with beginShape ():
                    vertex ((x + bottomPent[i + 2].x), (y + bottomPent[i + 2].y), (z + bottomPent[i + 2].z))
                    vertex ((x + topPent [i].x), (y + topPent [i].y), (z + topPent [i].z))
                    vertex ((x + topPent[i + 1].x), (y + topPent[i + 1].y), (z + topPent[i + 1].z))
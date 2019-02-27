class noiseBit(object):
    def __init__(self, index, xLeft, xRight, yTop, yBottom):
        self.index = index
        self.xL = xLeft
        self.xR = xRight
        self.yT = yTop
        self.yB = yBottom
        self.pos = PVector (random (self.xL, self.xR),
                            random (self.yT, self.yB),
                            random (-500, -250))
        self.speed = PVector (random(-noiseSpeed, noiseSpeed),
                              random(-noiseSpeed, noiseSpeed),
                              random(-noiseSpeed, noiseSpeed))
        self.c = color(random(255), random(255), random(255))

    def display(self):
        stroke(self.c)
        point(self.pos.x, self.pos.y, self.pos.z)

    def move (self):
        self.pos = self.pos + self.speed
        if self.pos.x <= self.xL or self.pos.x >= self.xR:
            self.speed.x = -self.speed.x
        if self.pos.y <= self.yT or self.pos.y >= self.yB:
            self.speed.y = -self.speed.y
        if self.pos.z <= -500 or self.pos.z >= -250:
            self.speed.z = -self.speed.z
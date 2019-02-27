// environmental variables
public int windowSize = 750;
public float sizeFactor = 0.3;
public int loopLength = 45;
public float tick = 0;
public float tick1 = 0;

// dots
public int dotDensity = 40;
public int nDots = dotDensity * dotDensity * dotDensity;
public dots [] goodShit;
public float speed = 2;


void setup() {
  size(750, 750, P3D);
  colorMode(HSB);
  //noiseDetail(5, 0.95);
  goodShit = new dots [nDots];
  for(int i = 0; i < goodShit.length; i++) {
    goodShit[i] = new dots(i);
  }
}

void draw() {
  background(15);
  
  tick += TWO_PI / loopLength;
  tick1 += 255 / loopLength;
  
  beginCamera();
    camera();
    translate(windowSize / 2, windowSize / 2, -1.25 * windowSize * sizeFactor);
    rotateX(QUARTER_PI);
    //rotateY(tick);
    //rotateY(HALF_PI);
    rotateZ(tick);
  endCamera();
  
  for(int i = 0; i < goodShit.length; i++) {
    goodShit[i].display();
    //goodShit[i].move();
  }
  
  pushMatrix();
    fill(15);
    noStroke();
    box(windowSize * sizeFactor * 1.875);
  popMatrix();
  
  /**/
  saveFrame("frames/###.png");
  if(frameCount >= loopLength) {
    exit();
  }
}

public class dots {
  
  private int index;
  private PVector position;
  private PVector velocity;
  private PVector field;
  private color c;
  
  public dots(int index_) {
    index = index_;
    position = new PVector(map(index % dotDensity, 0, dotDensity - 1, -windowSize * sizeFactor, windowSize * sizeFactor), map((index / dotDensity) % dotDensity, 0, dotDensity - 1, -windowSize * sizeFactor, windowSize * sizeFactor), map((index / dotDensity / dotDensity) % dotDensity, 0, dotDensity - 1, -windowSize * sizeFactor, windowSize * sizeFactor));
    velocity = new PVector();
  }
  
  void display() {
    c = color((255 * index / nDots + tick1 * 2) % 255, 50, 150, 75);
    stroke(c);
    strokeWeight(2);
    point(position.x, position.y, position.z);
  }
  
  void move() {
    field = gradient(position.x + windowSize, position.y + windowSize, position.z + windowSize + tick1);
    PVector k = new PVector(0, 0, 1);
    field.cross(k);
    velocity.add(field);
    position.add(velocity);
    
    if(abs(position.x) >= (windowSize * sizeFactor + 1)) {
      velocity.sub(2 * velocity.x, 0, 0);
    }
    
    if(abs(position.y) >= (windowSize * sizeFactor + 1)) {
      velocity.sub(0, 2 * velocity.y, 0);
    }
    
    if(abs(position.z) >= (windowSize * sizeFactor + 1)) {
      velocity.sub(0, 0, 2 * velocity.z);
    }
  }
}

public PVector gradient(float x, float y, float z) {
  float dx = (noise((x + 1) * 0.01, y * 0.01, z * 0.01) - noise((x - 1) * 0.01, y * 0.01, z * 0.01)) / sqrt(2) / 2;
  float dy = (noise(x * 0.01, (y + 1) * 0.01, z * 0.01) - noise(x * 0.01, (y - 1) * 0.01, z * 0.01)) / sqrt(2) / 2;
  float dz = (noise(x * 0.01, y * 0.01, (z + 1) * 0.01) - noise(x * 0.01, y * 0.01, (z - 1) * 0.01)) / sqrt(2) / 2;
  PVector del = new PVector(dx, dy, dz);
  return del;
}
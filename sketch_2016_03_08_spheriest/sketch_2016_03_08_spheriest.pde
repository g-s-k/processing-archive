// environment setup
public int windowSize = 750;
public int loopLength = 30;
public float tick1 = 0;
public float tick2 = 0;
public float mod1;
public float mod2;

// object setup
public int nDots = 90000;
public int pointDensity = 2880 * 2 + 1;
public pointDude [] goodShit;
public int nNoise = windowSize * windowSize;
public noiseDude [] badShit;

// processing runtime
void setup() {
  size(750,750,P3D);
  colorMode(HSB);
  noiseDetail(3, 0.65);
  goodShit = new pointDude [nDots];
  for(int i = 0; i < goodShit.length; i++) {
    goodShit[i] = new pointDude(i);
  }
  badShit = new noiseDude [nNoise];
  for(int j = 0; j < badShit.length; j++) {
    badShit[j] = new noiseDude(j);
  }
}

void draw() {
  // environment
  background(15);
  
  //modulation
  tick1 += TWO_PI / loopLength;
  tick2 += 255 / loopLength;
  mod1 = cos(tick1);
  mod2 = sin(tick1);
  
  
  // camera work
  beginCamera();
    camera();
    translate(windowSize / 2, windowSize / 2);
    rotateX(HALF_PI);
    //rotateY(-tick1);
    //rotateZ(tick1);
  endCamera();
  
  
  // object display
  for(int i = 0; i < goodShit.length; i++) {
    goodShit[i].move();
    goodShit[i].display();
  }
  
  for(int j = 0; j < badShit.length; j++) {
    badShit[j].display();
  }
  
  // render inner sphere
  pushMatrix();
    translate(0, 0, 0);
    fill(15);
    noStroke();
    sphere(windowSize * 0.3);
  popMatrix();
  
  /**/
  // save & exit
  saveFrame("frames/####.png");
  if(frameCount >= loopLength) {
    exit();
  }
  /**/
}

// line objects
public class pointDude {
  
  private float index;
  private float r_;
  private PVector position;
  private color c;
  private float rand;
  private float radius;
  private float phi;
  private float theta;
  
  public pointDude(float index_) {
    index = index_;
    r_ = windowSize * 0.3;
    theta = TWO_PI * pointDensity * index / nDots;
    phi = acos(2 * index / nDots - 1);
  }
  
  void display() {
    strokeWeight(2);
    stroke(c);
    point(position.x, position.y, position.z);
  }
  
  void move() {
    rand = noise(r_ * cos(theta - tick1) * sin(phi - tick1) * 0.01 + 50, r_ * sin(theta + tick1) * sin(phi) * 0.01 + 50, r_ * cos(phi + tick1) * 0.01 + 50);
    radius = r_ + rand * rand * rand * rand * windowSize * 0.075;
    position = new PVector(radius * cos(theta) * sin(phi), radius * sin(theta) * sin(phi), radius * cos(phi));
    c = color(255 * rand, 100, 25 + 125 * rand);
  }
}

// noise objects
public class noiseDude {
  
  private int index;
  
  public noiseDude(int index_) {
    index = index_;
    
  }
  
  void display() {
    
  }
}
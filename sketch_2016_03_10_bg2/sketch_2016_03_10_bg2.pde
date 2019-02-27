// environment setup
public int windowSize = 2000;
public int loopLength = 1;
public float tick1 = 0;
public float tick2 = 0;
public float mod1;
public float mod2;

// object setup
public int nDots = 700000;
public int pointDensity = 2880 * 2 + 1;
public int dudeDensity = 15;
public int nDudes = dudeDensity * dudeDensity;
public pointDude [] goodShit;
public noiseDude [] badShit;

// processing runtime
void settings() {
  size(windowSize * 16 / 9, windowSize, P3D);
}

void setup() {
  colorMode(HSB);
  noiseDetail(3, 0.99);
  goodShit = new pointDude [nDots];
  for(int i = 0; i < goodShit.length; i++) {
    goodShit[i] = new pointDude(i);
  }
  badShit = new noiseDude [nDudes];
  for(int j = 0; j < badShit.length; j++) {
    badShit[j] = new noiseDude(j);
  }
}

void draw() {
  // environment
  background(0);
  /*
  //modulation
  tick1 += TWO_PI / loopLength;
  tick2 += 255 / loopLength;
  mod1 = cos(tick1);
  mod2 = sin(tick1);
  */
  
  // camera work
  beginCamera();
    camera();
    translate(width / 2, height / 2);
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
    fill(0);
    noStroke();
    sphere(windowSize * 0.3);
  popMatrix();
  
  /**/
  // save & exit
  saveFrame("frames/####.jpg");
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
    strokeWeight(1);
    stroke(c);
    point(position.x, position.y, position.z);
  }
  
  void move() {
    rand = noise(r_ * cos(theta - tick1) * sin(phi - tick1) * 0.01 + 50, r_ * sin(theta + tick1) * sin(phi) * 0.01 + 50, r_ * cos(phi + tick1) * 0.01 + 50);
    radius = r_ + rand * rand * rand * rand * rand * rand * windowSize * (0.05 + random(0.025));
    position = new PVector(radius * cos(theta) * sin(phi), radius * sin(theta) * sin(phi), radius * cos(phi));
    c = color(255 * (((rand) % 0.1) * 10), 25 + 75 * (1 - rand), 0 + 175 * rand);
  }
}

// noise objects
public class noiseDude {
  
  private int index;
  private float rand;
  private PVector position;
  
  public noiseDude(int index_) {
    index = index_;
    rand = random(1);
    position = new PVector(width / dudeDensity * (index % dudeDensity + 0.5) - width / 2, 0, height / dudeDensity * ((index / dudeDensity) % dudeDensity + 0.5) - height / 2);
  }
  
  void display() {
    noFill();
    stroke(255 * index / nDudes, 50, 100, 50);
    strokeWeight(2);
    pushMatrix();
      translate(position.x, position.y, position.z);
      rotateX(rand * HALF_PI);
      rotateZ(rand * HALF_PI - QUARTER_PI);
      box(windowSize / 75);
    popMatrix();
  }
}
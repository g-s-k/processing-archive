// environment setup
public int windowSize = 750;
public int loopLength = 450;
public float tick1 = 0;
public float tick2 = 0;
public float mod1;

// object setup
public int nDots = 360000;
public int pointDensity = 360;
public pointDude [] goodShit;
public int nNoise = windowSize * windowSize;
public noiseDude [] badShit;

// processing runtime
void setup() {
  size(750,750,P3D);
  colorMode(HSB);
  noiseDetail(5, 0.5);
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
  
  // camera work
  beginCamera();
    camera();
    translate(windowSize / 2, windowSize / 2);
    rotateX(HALF_PI);
    rotateY(-tick1);
    rotateZ(tick1);
  endCamera();
  
  // object display
  for(int i = 0; i < goodShit.length; i++) {
    goodShit[i].display();
    goodShit[i].move();
  }
  for(int j = 0; j < badShit.length; j++) {
    badShit[j].display();
  }
  
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
  
  private int index;
  private PVector position;
  private color c;
  private float rand;
  private float radius;
  private float phi;
  private float theta;
  
  public pointDude(int index_) {
    index = index_;
    float r_ = windowSize * 0.15;
    theta = TWO_PI / pointDensity * (index % pointDensity);
    phi = TWO_PI * round(index / pointDensity - 0.5) / pointDensity - HALF_PI;
    rand = noise(r_ * sin(theta) * cos(phi) * 0.01 + 50, r_ * sin(theta) * sin(phi) * 0.01 + 50, r_ * cos(theta) * 0.01 + 50);
    radius = r_ + rand * windowSize * 0.25;
    position = new PVector(radius * sin(theta) * cos(phi), radius * sin(theta) * sin(phi), radius * cos(theta));
    c = color(255 * rand, 50, 25 + 125 * rand);
  }
  
  void display() {
    strokeWeight(2);
    stroke(c);
    point(position.x, position.y, position.z);
  }
  
  void move() {
    radius = radius * (1 + mod1);
    c = color((hue(c) + tick2) % 255, saturation(c), brightness(c));
    //position.x = radius * sin(theta) * cos(phi);
    //position.y = radius * sin(theta) * sin(phi);
    //position.z = radius * cos(phi);
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
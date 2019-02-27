// environment
public int windowHeight = 1080;
public int windowWidth = 1920;

// drawing setup
public int nDots = 260000;
public static int noiseDensity = 360;
public noiseBit [] goodShit;

void setup() {
  size(1920, 1080, P3D);
  colorMode(HSB);
  noiseDetail(5, 0.5);
  goodShit = new noiseBit [nDots];
  for(int i = 0; i < goodShit.length; i++) {
    goodShit[i] = new noiseBit(i);
  }
}

void draw() {
  background(15);
  
  // camera work
  beginCamera();
    camera();
    translate(windowWidth / 2, windowHeight / 2, 0);
    rotateX(HALF_PI);
    rotateZ(QUARTER_PI);
  endCamera();
  
  // display noise bits
  for(int i = 0; i < goodShit.length; i++) {
    goodShit[i].display();
  }
  
  // draw inner sphere
  noStroke();
  fill(20);
  pushMatrix();
    translate(0, 0, 0);
    sphere(windowHeight / 3 - windowHeight * 0.025);
  popMatrix();
  
  // save & exit
  saveFrame("frames/##.png");
  if(frameCount >= 1){
    exit();
  }
}

public class noiseBit {
  
  private int index;
  private PVector position;
  private float c;
  
  public noiseBit(int indexNum){
    index = indexNum;
    float phi = PI / noiseDensity * (index % noiseDensity);
    float theta = PI / noiseDensity * round(index / noiseDensity - 0.5);
    float h = map(windowHeight * 0.6 / noiseDensity * (index % noiseDensity), 0, index / noiseDensity, windowHeight * 0.2, windowHeight * 0.8);
    float randVal = noise(sin(phi) * cos(theta) * 3, sin(phi) * sin(theta) * 3, h * 0.001);
    float radius = windowHeight * 0.3 + randVal * windowHeight * 0.075;
    position = new PVector(radius * sin(phi) * cos(theta), radius * sin(phi) * sin(theta), radius * cos(phi));
    c = randVal * 255;
  }
  
  void display(){
    stroke(c, 35, c * 100 / 255);
    strokeWeight(2);
    point(position.x, position.y, position.z);
  }
}
// environment init
public static int windowSize = 750;
public static int loopLength = 75;

// object setup
public static int nDots = 260000;
public static int noiseDensity = 360;
public noiseBit[] goodShitA;

// modulation init
public float tick1 = 0;
public float tick2 = 0;
public float mod1;

// processing runtime
public void setup() {
  size(750, 750, P3D);
  colorMode(HSB);
  noiseDetail(5, 0.5);
  goodShitA = new noiseBit[nDots];
  for(int i = 0; i < goodShitA.length; i++){
    goodShitA[i] = new noiseBit(i);
  }
}

public void draw() {
  // environment
  background(20);
  
  // modulation
  tick1 += TWO_PI / loopLength;
  tick2 += 255 / loopLength;
  mod1 = sin(tick1);
  
  // camera placement & motion
  beginCamera();
    camera();
    translate(windowSize / 2, windowSize / 2, 0);
    rotateX(HALF_PI);
    rotateZ(tick1);
  endCamera();
  
  // draw noise
  for(int i = 0; i < goodShitA.length; i++){
    goodShitA[i].display();
  }
  
  // draw inner sphere
  noStroke();
  fill(20);
  pushMatrix();
    translate(0, 0, 0);
    rotateZ(-tick1);
    sphere(windowSize / 3 - windowSize * 0.025);
  popMatrix();
  
  // save & exit
  saveFrame("frames/###.png");
  if(frameCount >= loopLength){
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
    float randVal = noise(sin(phi) * cos(theta) * 3, sin(phi) * sin(theta) * 3, cos(phi) * 3);
    float radius = windowSize * 0.3 + randVal * windowSize * 0.075;
    position = new PVector(radius * sin(phi) * cos(theta), radius * sin(phi) * sin(theta), radius * cos(phi));
    c = randVal * 255;
  }
  
  void display(){
    stroke(c, 35, c * 100 / 255);
    strokeWeight(2);
    point(position.x, position.y, position.z);
  }
}
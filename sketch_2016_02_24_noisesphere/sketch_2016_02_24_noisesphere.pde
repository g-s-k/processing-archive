public int windowSize = 750;
public int loopLength = 90;
public int nDots = 12000;
public noiseBits[] goodShitA;
public float tick1 = 0;
public int redShift = 50;

public class noiseBits {
  
  private int indexNumber;
  private float c;
  private PVector position;
  
  public noiseBits(int index){
    indexNumber = index;
    noiseDetail(5, 0.5);
    float randVal = noise((indexNumber % windowSize) * 0.01, (round(indexNumber / windowSize)) * 0.01, random(-0.1, 0.1));
    c = randVal * 255;
    float phi = PI * index / nDots;
    float theta = TWO_PI * randVal * 2;
    float radius = windowSize * 0.3 + randVal * windowSize * 0.03;
    position = new PVector((radius * sin(phi) * cos(theta)), (radius * sin(phi) * sin(theta)), (radius * cos(phi)));
  }
  
  void display() {
    stroke(c, 255, c * 200 / 255 + 55);
    strokeWeight(2);
    point(position.x, position.y, position.z);
  }
}

void setup() {
  size(750, 750, P3D);
  colorMode(HSB);
  goodShitA = new noiseBits[nDots];
  for(int i = 0; i < goodShitA.length; i++) {
    goodShitA[i] = new noiseBits(i);
  }
}

void draw() {
  background(30);
  tick1 += TWO_PI / loopLength;
  
  //camera work
  beginCamera();
    camera();
    translate(windowSize / 2, windowSize / 2, 0);
    rotateX(HALF_PI);
    rotateZ(-tick1);
  endCamera();
  
  //draw sphere
  pushMatrix();
    fill(30);
    noStroke();
    sphere(windowSize * 0.3);
  popMatrix();
  
  //draw points
  for(int i = 0; i < goodShitA.length; i++) {
    goodShitA[i].display();
  }  
  
  //save & exit
  saveFrame("frames/#####.tiff");
  if(frameCount >= loopLength) {
    exit();
  }
}
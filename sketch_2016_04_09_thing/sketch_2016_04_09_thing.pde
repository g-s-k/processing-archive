//environment
public static int windowSize = 500;
public static int loopLength = 60;
public float tic1 = 0;
public float tic2 = 0;
public float mod1 = 0;
public float mod2 = 1;

//objects
public int dim = 99;
public float sizeFactor = 0.3;
public int nDots = dim * dim * dim;
public dots [] goodShit;

//processing runtime
void settings(){
  size(windowSize, windowSize, P3D);
}
void setup(){
  colorMode(HSB);
  noiseDetail(5, 0.999999999999999999999);
  //frameRate(15);
  goodShit = new dots [nDots];
  for(int i = 0; i < goodShit.length; i++) {
    goodShit[i] = new dots(i);
  }
  //background(15);
}
void draw(){
  //environment
  background(15);
  //camera
  beginCamera();
    camera();
    translate(windowSize/2, windowSize/2, -1 * windowSize * sizeFactor);
    rotateX(QUARTER_PI);
    rotateY(0);
    rotateZ(QUARTER_PI + 0.1 + tic1);
  endCamera();
  //object renders
  for(int i = 0; i < goodShit.length; i++) {
    goodShit[i].display();
  }
  /**/
  //save & exit
  saveFrame("frames/###.png");
  if(frameCount >= loopLength){
    exit();
  }
  /**/
  //modulation
  tic1 += TWO_PI / loopLength;
  tic2 += 255 / loopLength;
  mod1 = sin(tic1);
  mod2 = cos(tic1);
}

//class & function
public class dots{
  //declarations
  private int index;
  private float rand;
  private PVector position;
  private color c;
  //constructor
  public dots(int i){
    index = i;
    position = new PVector(map(index % dim, 0, dim - 1, -windowSize * sizeFactor, windowSize * sizeFactor), map((index / dim) % dim, 0, dim - 1, -windowSize * sizeFactor, windowSize * sizeFactor), map((index / dim / dim) % dim, 0, dim - 1, -windowSize * sizeFactor, windowSize * sizeFactor));
    rand = noise(position.x * 0.01, position.y * 0.01, position.z * 0.01);
  }
  //display() method
  void display(){
    c = color(map(rand, 0, 2, 0, 255), 50 * rand, 250, 200);
    stroke(c);
    strokeWeight(1);
    point(position.x, position.y, position.z + map(rand, 0, 2, -windowSize*sizeFactor, windowSize*sizeFactor) * mod1);
  }
}
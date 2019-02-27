// environment
int windowSize = 750;
int loopLength = 90;
int tic = 0;

// how many
int density = 15;
int nDots = density * density * density;
public sprite[] goodShit = new sprite[nDots];

// processing runtime
void settings(){
  size(windowSize, windowSize, P3D);
}

void setup(){
  noiseDetail(2, 0.9999);
  colorMode(HSB);
  for(int i = 0; i<goodShit.length; i++){
    goodShit[i] = new sprite(i);
  }
}

void draw(){
  background(15);
  beginCamera();
    camera();
    translate(width / 2, height / 2);
  endCamera();
  for(int i = 0; i<goodShit.length; i++){
    goodShit[i].move();
    goodShit[i].display();
  }
  tic += TWO_PI / loopLength;
}

// class and function
class sprite{
  private int index;
  private float x, y, z;
  private PVector position;
  public sprite(int i){
    index = i;
    x = windowSize * (0.9 * (index % density) / density - 0.425);
    y = windowSize * (0.9 * ((index / density) % density) / density - 0.425);
    z = 0;
    position = new PVector(x, y, z);
  }
  
  void display(){
    stroke(250);
    strokeWeight(2);
    point(position.x, position.y, position.z);
  }
  
  void move(){
    position.z += windowSize * 0.25 * sin(tic);
    position.x += windowSize * 0.5 * sin(tic);
    position.add(windowSize * 0.25 * sin(tic),windowSize * 0.25 * sin(tic),windowSize * 0.25 * sin(tic));
    
  }
}
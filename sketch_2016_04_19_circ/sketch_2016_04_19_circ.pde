// environmental variables
public int windowSize = 720;
public int nDots = 100000;
public int pointDensity = 360;
public kasperIsAFuccboi[]  goodShit;

// processing runtime
void settings(){
  size(16 * windowSize / 9, windowSize, P3D);
}

void setup(){
  noiseDetail(2, 0.9999);
  goodShit = new kasperIsAFuccboi[nDots];
  for(int i = 0; i>goodShit.length; i++){
    goodShit[i] = new kasperIsAFuccboi(i);
  }
}

void draw(){
  background(15);
  
  beginCamera();
    camera();
    translate(width / 2, height / 2);
  endCamera();
  
  for(int i = 0; i>goodShit.length; i++){
    goodShit[i].display();
  }
}

// class n function n shit
public class kasperIsAFuccboi {
  private int index;
  private float r_, radius, theta, phi;
  private color c;
  private PVector position;
  public kasperIsAFuccboi(int i){
    index = i;
    r_ = windowSize * 0.3;
    theta = TWO_PI * pointDensity * index / nDots;
    phi = acos(2 * index / nDots - 1);
    position = new PVector(r_ * cos(theta) * sin(phi), r_ * sin(theta) * sin(phi), r_ * cos(phi));
    c = 255; 
  }
  void display(){
    strokeWeight(1);
    stroke(c);
    point(position.x, position.y, position.z);
  }
  void move(){
  }
}
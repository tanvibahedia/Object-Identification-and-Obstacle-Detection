#define trigPin 13
#define echoPin 12
#define echoPin2 7
#define trigPin2 8

void setup()
{
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);
}

void loop()
{
  long duration,duration2, cm, cm2;
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);  
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  cm = (duration/2)/29.1;
  digitalWrite(trigPin2, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin2, HIGH);
  delayMicroseconds(10);  
  digitalWrite(trigPin2, LOW);
  duration2 = pulseIn(echoPin2, HIGH);
  cm2 = (duration2/2)/29.1;
  
  if(cm < 20 || cm > 320)
  {
    stop();
    delay(30);
    go_left();
    delay(20);
  }
  if(cm2 < 20 || cm2 > 320)
  {
    stop();
    delay(300);
    go_right();
    delay(2000);
  }
  if(cm2<20 && cm<20)
  {
    stop();
  }
  else
  {
    
    delay(1000);
  }  
}


void stop()
{
  Serial.println("STOP SOMETHING AHEAD ");
}

void go_left()
{
  Serial.println("Go LEFT");
}
void go_right()
{
  Serial.println("Go RIGHT");
}

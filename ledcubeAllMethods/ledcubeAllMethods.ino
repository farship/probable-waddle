int timeDelay = 250;
int pattern = 0;
void setup() {
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
  for(int i=2;i<13;i++) {
    digitalWrite(i, LOW);}
}

void loop() {
  if (pattern == 1) {
  for(int u=2;u<11;u++){
    if (u != 2) {
      digitalWrite(u-1, LOW);
    }
    digitalWrite(u, HIGH);
    transSingle();
  }
  digitalWrite(10, LOW);
  }
  if (pattern == 2) {
  for(int u=2;u<11;u++){
    if (u != 2) {
      digitalWrite(u-1, LOW);
    }
    digitalWrite(u, HIGH);
    transSingle();
  }
  reverse();
  }
  if (pattern == 3) {
  for(int u=2;u<11;u++){
    if (u != 2) {
      digitalWrite(u-1, LOW);
    }
    digitalWrite(u, HIGH);
    transTriple();
  }
  digitalWrite(10, LOW);
  }
  if (pattern == 5) {
    timeDelay = 250;
  }
  if (pattern == 6) {
    timeDelay = 150;
  }
  if (pattern == 7) {
    timeDelay = 50;
  }
  checkPattern();
  if (pattern == 0) {
    delay(250);
  }
}

void transSingle() {
  digitalWrite(11, HIGH);
  delay(timeDelay);
  digitalWrite(11, LOW);
  digitalWrite(12, HIGH);
  delay(timeDelay);
  digitalWrite(12, LOW);
  digitalWrite(13, HIGH);
  delay(timeDelay);
  digitalWrite(13, LOW);
}

void transTriple() {
  digitalWrite(11, HIGH);
  digitalWrite(12, HIGH);
  digitalWrite(13, HIGH);
  delay(timeDelay);
}

void reverseTransSingle() {
  digitalWrite(13, HIGH);
  delay(timeDelay);
  digitalWrite(13, LOW);
  digitalWrite(12, HIGH);
  delay(timeDelay);
  digitalWrite(12, LOW);
  digitalWrite(11, HIGH);
  delay(timeDelay);
  digitalWrite(11, LOW);
}

void reverse() {
  for(int z=10;z>1;z--) {
    if (z != 10) {
      digitalWrite(z+1, LOW);
    }
    digitalWrite(z, HIGH);
    reverseTransSingle();
  }
}

void checkPattern() {
  int patternPinA0 = analogRead(A0);
  int patternPinA1 = analogRead(A1);
  int patternPinA2 = analogRead(A2);
  int patternPinA3 = analogRead(A3);
  
  int patternPinA5 = analogRead(A5);
  int patternPinA6 = analogRead(A6);
  int patternPinA7 = analogRead(A7);
  if (patternPinA0 == 692 || patternPinA0 == 1023) {
    pattern = 0;
  }
  else if (patternPinA1 == 692 || patternPinA1 == 1023) {
    pattern = 1;
  }
  else if (patternPinA2 == 692 || patternPinA2 == 1023) {
    pattern = 2;
  }
  else if (patternPinA3 == 692 || patternPinA3 == 1023) {
    pattern = 3;
  }
  else if (patternPinA5 == 692 || patternPinA5 == 1023) {
    pattern = 5;
  }
  else if (patternPinA6 == 692 || patternPinA6 == 1023) {
    pattern = 6;
  }
  else if (patternPinA7 == 692 || patternPinA7 == 1023) {
    pattern = 7;
  }
  else {pattern = 0;}
}

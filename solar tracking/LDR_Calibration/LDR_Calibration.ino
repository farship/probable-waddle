const int ldrNWPin = A6;
const int ldrSWPin = A4;
const int ldrNEPin = A2;
const int ldrSEPin = A0;

int ldrNWValue;
int ldrSWValue;
int ldrNEValue;
int ldrSEValue;

void setup() {
    Serial.begin(9600);
    Serial.print("SETUP");
}

void loop() {
    ldrNWValue = 1.045*analogRead(ldrNWPin);
    Serial.print ("NW: ");
    Serial.print (ldrNWValue);
    Serial.print ('\n');

    ldrSWValue = analogRead(ldrSWPin);
    Serial.print ("SW: ");
    Serial.print (ldrSWValue);
    Serial.print ('\n');

    Serial.print ("        NW-SW= ");
    Serial.print (ldrNWValue - ldrSWValue);
    Serial.print ('\n');
    
    ldrNEValue = 0.92*analogRead(ldrNEPin);
    Serial.print ("NE: ");
    Serial.print (ldrNEValue);
    Serial.print ('\n');

    ldrSEValue = analogRead(ldrSEPin);
    Serial.print ("SE: ");
    Serial.print (ldrSEValue);
    Serial.print ('\n');

    Serial.print ("        NE-SE= ");
    Serial.print (ldrNEValue - ldrSEValue);
    Serial.print ('\n');
    
    delay(1000);
}

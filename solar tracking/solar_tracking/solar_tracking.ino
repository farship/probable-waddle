#include <Servo.h>

//Creating servo object to be controlled
Servo servoNS; //up and down servo object
int servoNS_Pos = 90; //position of servo in degrees, 5-175
Servo servoEW; //left and right servo object
int servoEW_Pos = 90; //position of servo in degrees, 5-175

//Pins
const int ldrNE = A2; //uses analog pins 1-4
const int ldrSE = A0;
const int ldrSW = A4;
const int ldrNW = A6;

const double ldrNWCoefficient = 1.045;
const double ldrNECoefficient = 0.92;

int ldrNW_Vol;
int ldrSW_Vol;
int ldrW_VolDif;

int ldrNE_Vol;
int ldrSE_Vol;
int ldrE_VolDif;

void setup() {
    Serial.begin (9600); //starts monitor
    Serial.print ("SETUP");
    pinMode(ldrNE, INPUT); //sets all LDRs as inputs
    pinMode(ldrSE, INPUT);
    pinMode(ldrSW, INPUT);
    pinMode(ldrNW, INPUT);

    servoNS.attach(3); //pin of NS servo, up and down
    servoEW.attach(2); //pin of EW servo, left and right
}

void loop() {
    ldrNW_Vol = ldrNWCoefficient * analogRead(ldrNW); //gets relative voltage through NW LDR
    ldrSW_Vol = analogRead(ldrSW); //gets relative voltage through SW LDR
    ldrW_VolDif = ldrNW_Vol - ldrSW_Vol; //finds difference between rel. vol. Posative value means north has more light. Negative value means south has more light.
    if (ldrW_VolDif > 5) { //reduces jittering on boundary
        if (servoNS_Pos < 175) { //stops current draw beyond true reach of motor
            servoNS_Pos++;
            servoNS.write(servoNS_Pos);
            delay(10);
        }
    }
    else if (ldrW_VolDif < -5) { //reduces jittering on boundary
        if (servoNS_Pos > 5) { //stops current draw beyond true reach of motor
            servoNS_Pos--;
            servoNS.write(servoNS_Pos);
            delay(10);
        }
    }

    
    ldrNE_Vol = ldrNECoefficient * analogRead(ldrNE);//ldrNECoefficient 0.92* analogRead(ldrNE);
    ldrSE_Vol = analogRead(ldrNW);//change name here and be references
    ldrE_VolDif = ldrNE_Vol - ldrSE_Vol;
    Serial.print("E_VolDif:");
    Serial.print(ldrE_VolDif);
    if (ldrE_VolDif > 5) { //reduces jittering on boundary
        if (servoEW_Pos < 175) { //stops current draw beyond true reach of motor
            servoEW_Pos++;
            servoEW.write(servoEW_Pos);
            delay(10);
        }
    }
    else if (ldrE_VolDif < -5) { //reduces jittering on boundary
        if (servoEW_Pos > 5) { //stops current draw beyond true reach of motor
            servoEW_Pos--;
            servoEW.write(servoEW_Pos);
            delay(10);
        }
    }
    

/*    Serial.print ("NW: ");
    Serial.print(ldrNW_Vol);
    Serial.print("\n");
    Serial.print ("SW: ");
    Serial.print(ldrSW_Vol);
    Serial.print("\n");
    Serial.print ("NE: ");
    Serial.print(ldrNE_Vol);
    Serial.print("\n");
    Serial.print ("SE: ");
    Serial.print(ldrSE_Vol);
    Serial.print("\n");
*/  
/*
    Serial.print("West-side: ");
    Serial.print(ldrW_VolDif);
    Serial.print("\n");
    Serial.print("East-side: ");
    Serial.print(ldrE_VolDif);
    Serial.print("\n");
 */ 
    Serial.print("Servo NS Posision: ");
    Serial.print(servoNS_Pos);
    Serial.print("\n");
    Serial.print("Servo EW Posision: ");
    Serial.print(servoEW_Pos);
    Serial.print("\n");
    delay(250); //LDRs only report every 30ms anyway and need processing and movement time
}

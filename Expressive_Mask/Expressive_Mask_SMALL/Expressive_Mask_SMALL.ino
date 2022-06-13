/*
 * Pattern is selected with IR Remote and Sensor - limited to 21 patterns without mode switching
 * 
 + Add Labels to the remote - with the expression or just numbers
 + increase intensity to 7
*/

#include <Adafruit_GFX.h>
#include <TM1640.h>
#include <TM16xxMatrixGFX.h>
#include "IRremote.h"

TM1640 module(8, 9);    // "For ESP8266/WeMos D1-mini: DIN=D7/13/MOSI, CLK=D5/14/SCK" // 8 : white : SDA (data), 9 : brown : SCL(clock)
#define MATRIX_NUMCOLUMNS 16
#define MATRIX_NUMROWS 8
TM16xxMatrixGFX matrix(&module, MATRIX_NUMCOLUMNS, MATRIX_NUMROWS);    // TM16xx object, columns, rows

IRrecv irrecv(11);     // create instance of 'irrecv' with pin 11
decode_results results;      // create instance of 'decode_results'

int expression = 0;
int irPattern = 0;

void setup() {
  irrecv.enableIRIn(); // Starts the IR receiver
  matrix.setRotation(3); // rotates the matrix array to match the module
  matrix.setMirror(false,true); // flips on y-axis for letters
  matrix.setIntensity(6);         // Use a value between 0 and 7 for brightness
  matrix.fillScreen(LOW);         // Clear the matrix
  matrix.write();                 // Send the memory bitmap to the display
}

void loop() {
  if (irrecv.decode(&results)) { // if IR signal recieved
    int newExpression = translateIR();
    if (newExpression != expression) { // reduces load
      expression = newExpression;
      setMemoryBufferPattern(expression); // build memory buffer with arrays
      matrix.write(); // draws the expression
    }
    irrecv.resume(); // receive the next value
  }
  delay(100);
}

int translateIR() { // translates IR Codes to the Buttons Pressed
  switch(results.value) {
  case 0xFFA25D: irPattern = 0;    break;  // POWER
  case 0xFF629D: irPattern = 1;    break;  // VOL+
  case 0xFFE21D: irPattern = 2;    break;  // FUNC/STOP
  case 0xFF22DD: irPattern = 3;    break;  // FAST BACK
  case 0xFF02FD: irPattern = 4;    break;  // PAUSE
  case 0xFFC23D: irPattern = 5;    break;  // FAST FORWARD
  case 0xFFE01F: irPattern = 6;    break;  // DOWN
  case 0xFFA857: irPattern = 7;    break;  // VOL-
  case 0xFF906F: irPattern = 8;    break;  // UP
  case 0xFF6897: irPattern = 9;    break;  // 0
  case 0xFF9867: irPattern = 10;   break;  // EQ
  case 0xFFB04F: irPattern = 11;   break;  // ST/REPT
  case 0xFF30CF: irPattern = 12;   break;  // 1
  case 0xFF18E7: irPattern = 13;   break;  // 2
  case 0xFF7A85: irPattern = 14;   break;  // 3
  case 0xFF10EF: irPattern = 15;   break;  // 4
  case 0xFF38C7: irPattern = 16;   break;  // 5
  case 0xFF5AA5: irPattern = 17;   break;  // 6
  case 0xFF42BD: irPattern = 18;   break;  // 7
  case 0xFF4AB5: irPattern = 19;   break;  // 8
  case 0xFF52AD: irPattern = 20;   break;  // 9
  /*case 0xFFFFFFFF: Serial.println(" REPEAT");break; */ // repeat button press?
  
  default: 
    irPattern = irPattern;
  }
  return irPattern; 
}

void fillMemoryBuffer(int arrayPattern[8][16]) {
  for(int xLEDCoord = 0; xLEDCoord < 16; xLEDCoord++) {
    for(int yLEDCoord = 0; yLEDCoord < 8; yLEDCoord++) {
      if(arrayPattern[yLEDCoord][xLEDCoord] == 0) {
        matrix.drawPixel(xLEDCoord,yLEDCoord, LOW);}
      if(arrayPattern[yLEDCoord][xLEDCoord] == 1) {
        matrix.drawPixel(xLEDCoord,yLEDCoord, HIGH);}
      }
    }
}

void setMemoryBufferPattern(int pattern) {
  if(pattern == 0) { // Blank
    matrix.fillScreen(LOW);
  }
  if (pattern == 1) { // sad
    int litXYLEDs[8][16] {
      {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
      {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
      {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0},
      {0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0},
      {0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0},
      {0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0},
      {0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0},
      {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}};
    fillMemoryBuffer(litXYLEDs);
  }
  if (pattern == 2) {  // *Ok then...*
    int litXYLEDs[8][16] {
      {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
      {1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1},
      {0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0},
      {0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0},
      {0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0},
      {0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0},
      {1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1},
      {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1}};
    fillMemoryBuffer(litXYLEDs);
  }
  /*if (pattern == 3) { // *OH* - O
    int litXYLEDs[8][16] {
      {0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0},
      {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0},
      {0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0},
      {0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0},
      {0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0},
      {0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0},
      {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0},
      {0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0}};
    fillMemoryBuffer(litXYLEDs);
  }*/
  if (pattern == 4) { // Happy - Wholesome/Cute
    int litXYLEDs[8][16] {
      {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
      {0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0},
      {0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0},
      {0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0},
      {0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0},
      {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0},
      {0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0},
      {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}};
    fillMemoryBuffer(litXYLEDs);
  }
  if (pattern == 5) { // Heart Face - < v >
    int litXYLEDs[8][16] {
      {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
      {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
      {0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0},
      {0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0},
      {0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0},
      {0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0},
      {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
      {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}};
    fillMemoryBuffer(litXYLEDs);
  }
  if (pattern == 6) { // Big Heart
    int litXYLEDs[8][16] {
      {0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0},
      {0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0},
      {0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0},
      {0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0},
      {0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0},
      {0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0},
      {0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0},
      {0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0}};
    fillMemoryBuffer(litXYLEDs);
  }
  if (pattern == 7) {  // I <3 U
    int litXYLEDs[8][16] {
      {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
      {1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1},
      {0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1},
      {0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1},
      {0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1},
      {0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1},
      {1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0},
      {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}};
    fillMemoryBuffer(litXYLEDs);
  }
  /*if (pattern == 8) { // F x K
    int litXYLEDs[8][16] {
      {1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0},
      {1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1},
      {1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1},
      {1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0},
      {1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0},
      {1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0},
      {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1},
      {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1}};
    fillMemoryBuffer(litXYLEDs);
  }*/
  if (pattern == 9) { // F U K
    int litXYLEDs[8][16] {
      {1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0},
      {1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1},
      {1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1},
      {1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0},
      {1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0},
      {1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0},
      {1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1},
      {1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1}};
    fillMemoryBuffer(litXYLEDs);
  }
  /*if (pattern == 10) { // C U M
    int litXYLEDs[8][16] {
      {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
      {0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0},
      {1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1},
      {1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1},
      {1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1},
      {1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1},
      {0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1},
      {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}};
    fillMemoryBuffer(litXYLEDs);
  }*/
  if (pattern == 11) { // 4 0 4
    int litXYLEDs[8][16] {
      {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
      {0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0},
      {0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0},
      {0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0},
      {1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1},
      {0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0},
      {0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0},
      {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}};
    fillMemoryBuffer(litXYLEDs);
  }
  /*if (pattern == 12) { // Suki Katakana
    int litXYLEDs[8][16] {
      {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
      {1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0},
      {0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1},
      {0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0},
      {0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0},
      {0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1},
      {0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0},
      {1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0}};
    fillMemoryBuffer(litXYLEDs);
  }
}*/
/* template
if (pattern == ) {
    int litXYLEDs[8][16] {
      {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
      {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
      {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
      {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
      {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
      {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
      {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
      {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}};
    fillMemoryBuffer(litXYLEDs);
  }
*/

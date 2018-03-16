/** 
 *  Author: Ryan Frazier
 *  Date: Feb 3, 2018
 *  
 *  This is free and unencumbered software released into the public domain.
 *
**/

const int N_PINS = 4;
const int buttonPin = 9;

int pins[] = {2,3,4,5};
int mask = 0;
int buttonState = 0;
int lastButtonState = 0;

void setup() {                
  for(int i=0; i < N_PINS; i++) {
    pinMode(pins[i], OUTPUT);
  } 
  pinMode(buttonPin, INPUT_PULLUP);
}

void loop() {
  buttonState = digitalRead(buttonPin);
  if(buttonState != lastButtonState && buttonState == HIGH) {
    mask++;
    if (mask > 15) mask = 0;
    delay(50); // to avoid bouncing
  }
  lastButtonState = buttonState;
  for(int i = 0; i < N_PINS; i++) {
    digitalWrite(pins[i], (mask >> i) & 1);
  }
}

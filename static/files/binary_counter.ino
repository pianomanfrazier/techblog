const int N_PINS = 4;
int pins[] = {2,3,4,5};
int mask = 0;

void setup() {                
  for(int i=0; i < N_PINS; i++) {
    pinMode(pins[i], OUTPUT);
  } 
}

void loop() {
  for(int i = 0; i < N_PINS; i++) {
    digitalWrite(pins[i], (mask >> i) & 1);
  }
  delay(1000);
  mask++;
  if (mask > 15) mask = 0;
}

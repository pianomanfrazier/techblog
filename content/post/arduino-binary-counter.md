---
title: "Arduino Binary Counter"
date: 2018-01-25T09:33:40-07:00
draft: false
markup: mmark
---

I am volunteering for a little science group once a week for my daughter's 1^st^ grade class. I thought it would be fun to learn to count binary so I programed an LED binary counter using an arduino. I am using an Arduino Mini Pro 3.3V.

{{< youtube FtFQ3j5bJoc >}}

For reference, the following table shows the binary representation of the base 10 digits 0 to 15. [Endianness](https://en.wikipedia.org/wiki/Endianness) has to do with the order the bits are stored. In this case I have chosen the smallest digit to be the first bit. So the digit 1~10~ would be `1000` using 4 bits.

Digit (base 10) | binary (little endian) | binary (big endian) |
----------------|------------------------|---------------------:
 0  | 0000 | 0000
 1  | 1000 | 0001
 2  | 0100 | 0010
 3  | 1100 | 0011
 4  | 0010 | 0100
 5  | 1010 | 0101
 6  | 0110 | 0110
 7  | 1110 | 0111
 8  | 0001 | 1000
 9  | 1001 | 1001
 10 | 0101 | 1010
 11 | 1101 | 1011
 12 | 0011 | 1100
 13 | 1011 | 1101
 14 | 0111 | 1110
 15 | 1111 | 1111

And here is the source. The trick is the bit masking part. Since the integer is already in binary form we just have to extract out the 0 or 1 from the right location with `(mask >> i) & 1`.

~~~c
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
~~~
[[download file]](/files/binary_counter.ino)

{{<figure title="Binary Counter Schematic" src="/img/binary_counter.png" caption="Binary Counter Schematic">}}


I then wanted to add a button to increment the count.

~~~c
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
  pinMode(buttonPin, INPUT);
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
~~~
[[download file]](/files/binary_counter_with_button.ino)

{{<figure title="Binary Counter Schematic with button" src="/img/binary_counter_with_button.png" caption="Binary Counter with Button Schematic">}}


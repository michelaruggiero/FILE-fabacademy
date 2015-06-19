#include <Servo.h>

Servo myservo;


long nextCalc;                // When we next calc the wind speed
long time;                    // Millis() at each start of loop().
#define RefreshRate   500 //RefreshTime

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  myservo.attach(6);                          //Il Pin del servo lo collego al Pin6\

}

void loop() {
  // put your main code here, to run repeatedly:
  time = millis();
  serialIn();
  if (time >= nextCalc) { //Non voglio saturare la seriale con le letture, ma non voglio nemmeno usare delay() perche' potrei perdere dati in ingresso...
    serialOut();
    nextCalc = time + RefreshRate;
  }
}

void serialOut() {
  Serial.write("P");
  byte dati2 = map(analogRead(A0),0,1024,0,255);
  Serial.write(dati2);
}

void serialIn() {
  while (Serial.available() > 1) {  //Aspetto che nel buffer ci siano almeno 2 bytes
    switch (Serial.read()) {    //Controllo il primo, deve essere un comando
      case 'A':
          myservo.write(100);

        break;
      case 'B':
          myservo.write(0);

        break;
    }
  }
}


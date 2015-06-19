int sensorValue = A0;
 
void setup() {
  pinMode(13,OUTPUT);
  Serial.begin(9600);
  Serial.print("sensor = " );
  //pinMode(6, INPUT);
}
 
void loop() {
  digitalWrite(13,HIGH);
  sensorValue = analogRead(A0);            
 
  Serial.print("sensor = " );
  Serial.println(sensorValue);      
 
  delay(1000);
  }
  

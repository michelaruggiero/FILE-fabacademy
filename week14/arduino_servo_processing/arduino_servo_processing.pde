
import processing.serial.*; // Aggiungo librerie: firmadata, arduino e seriale
Serial myPort;        // The serial port
void setup() {
  size(360,180); // dimensioni finestra
    for(int i=0; i <Serial.list().length;i++){
 //  println("["+ i +"] " + Serial.list()[i]); 
  }
   myPort = new Serial(this, Serial.list()[7], 9600);

  }

void draw() {
  int gradi = mouseX/2; // posizione del servo
 // String valore = str(gradi); // stringa da stampare
 String valore = gradi + "\n"; // stringa da stampare
 println(valore);
  myPort.write(valore);

  // Debug
  // println(mouseX); // verifica posizione mouse
  // println(gradi); // verifica conversione gradi
  // println(valore); // verifica stringa da stampare

  background(gradi); // colore di sfondo. IMPORTANTE!!!
  
  textSize(32); // dimensione del testo
  textAlign(CENTER); // allineamento del testo
  text(valore, 360/2, 180/2); // stampo il valore (rotazione in gradi)

}
void serialEvent (Serial myPort) {
 // get the ASCII string:
String inString = myPort.readStringUntil('\n');
 
 if (inString != null) {
 // trim off any whitespace:
 inString = trim(inString);
 println("received : " + inString);
 }
}


// from Seeed Studio documentation: https://wiki.seeedstudio.com/XIAO_ESP32C3_Getting_Started/
// define led according to pin diagram in article
const int led = 10; // there is no LED_BUILTIN available for the XIAO ESP32C3. //Ger changed this to GPIO10

void setup() {
  // initialize digital pin led as an output
  pinMode(led, OUTPUT);
}

void loop() {
  digitalWrite(led, HIGH);   // turn the LED on 
  delay(1000);               // wait for a second
  digitalWrite(led, LOW);    // turn the LED off
  delay(1000);               // wait for a second
}
// define led according to pin diagram in article
const int led1 = 9;     // GREEN
const int led2 = 8;     // GREEN
const int led3 = 10;    // YELLOW
const int led4 = D6;    // GREEN
const int led5 = D0;     // GREEN
const int led6 = D4;     // RED
const int button1 = D1;  // Button
const int button2 = D1;  // Button

void setup() {
  // initialize digital pin led as an output
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(led5, OUTPUT);
  pinMode(led6, OUTPUT);
  pinMode(button1, INPUT);
  pinMode(button2, INPUT);
}

void loop() {
  digitalWrite(led1, HIGH);  // turn the LEDs on
  delay(200);
  digitalWrite(led2, HIGH);
  delay(200);
  digitalWrite(led3, HIGH);
  delay(200);
  digitalWrite(led4, HIGH);
  delay(200);
  digitalWrite(led5, HIGH);
  delay(200);
  digitalWrite(led6, HIGH);
  //if (button1) {
  //  digitalWrite(led6, HIGH);
  //}
  delay(900);              // wait for a second
  digitalWrite(led1, LOW);  // turn the LEDs off
  digitalWrite(led2, LOW);
  digitalWrite(led3, LOW);
  digitalWrite(led4, LOW);
  digitalWrite(led5, LOW);
  digitalWrite(led6, LOW);
  delay(500);  // wait for a second
}
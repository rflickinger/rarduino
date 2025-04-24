void setup() {
    Serial.begin(9600); // Start serial communication
  }
  
  void loop() {
    int moisture = analogRead(A0); // Replace with your sensor pin
    Serial.println(moisture);      // Send data as plain text
    delay(1000);                   // Send every 1 second
  }
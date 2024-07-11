
const int relayPins[] = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11};

void setup() {
  Serial.begin(115200);

  // Set relay pins as OUTPUT
  for (int i = 0; i < 10; i++) {
    pinMode(relayPins[i], OUTPUT);
    // Initially turn off all relays
    digitalWrite(relayPins[i], HIGH); // Change LOW to HIGH
  }
}

void loop() {
  if (Serial.available() > 0) {
    char receivedChar = Serial.read();

    switch (receivedChar) {
      case '0':
        controlRelay(0, LOW); // Change HIGH to LOW
        controlRelay(1, LOW); // Change HIGH to LOW
        controlRelay(2, LOW); // Change HIGH to LOW
        controlRelay(3, LOW); // Change HIGH to LOW
        controlRelay(4, LOW); // Change HIGH to LOW
        
        delay(5000); 
        turnOffRelays();
        break;

      case '1':
        controlRelay(0, LOW); // Change HIGH to LOW
        controlRelay(2, LOW); // Change HIGH to LOW
        controlRelay(3, LOW); // Change HIGH to LOW
        controlRelay(4, LOW); // Change HIGH to LOW

        delay(5000); 
        turnOffRelays();
        break;
      
      case '2':
        controlRelay(0, LOW); // Change HIGH to LOW
        controlRelay(3, LOW); // Change HIGH to LOW
        controlRelay(4, LOW); // Change HIGH to LOW

        delay(5000);

        controlRelay(0, HIGH); // Change LOW to HIGH
        controlRelay(3, HIGH); // Change LOW to HIGH
        controlRelay(4, HIGH); // Change LOW to HIGH
        break;

      case '3':
        controlRelay(0, LOW); // Change HIGH to LOW
        controlRelay(4, LOW); // Change HIGH to LOW
        
        delay(5000);
        turnOffRelays();
        break;

      case '4':
        controlRelay(4, LOW); // Change HIGH to LOW
         
        delay(5000);
        turnOffRelays();
        break;

      case '5':
        turnOffRelays();
        break;

      case 'o':
        for (int i = 5; i < 10; i++) {
            controlRelay(i, LOW); // Change HIGH to LOW
        }
        break;
    }
  }
}

void controlRelay(int relayIndex, int state) {
  
  if (relayIndex >= 0 && relayIndex < 8) {
    digitalWrite(relayPins[relayIndex], state);
  }
}

void turnOffRelays() {
  // Turn off all relays
  for (int i = 0; i < 10; i++) {
    digitalWrite(relayPins[i], HIGH);
  }
}
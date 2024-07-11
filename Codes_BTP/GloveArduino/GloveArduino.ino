const int flexSensorPin1 = A1;
const int flexSensorPin2 = A2;
const int flexSensorPin3 = A3;
const int flexSensorPin4 = A4;
const int flexSensorPin5 = A5;


void setup() {
  Serial.begin(9600);
  pinMode(flexSensorPin1, INPUT);
  pinMode(flexSensorPin2, INPUT);
  pinMode(flexSensorPin3, INPUT);
  pinMode(flexSensorPin4, INPUT);
  pinMode(flexSensorPin5, INPUT);
}

void loop() {
  
  int flexValue1 = analogRead(flexSensorPin1); 
  int flexValue2 = analogRead(flexSensorPin2);
  int flexValue3 = analogRead(flexSensorPin3);
  int flexValue4 = analogRead(flexSensorPin4);
  int flexValue5 = analogRead(flexSensorPin5);
  
  Serial.print(flexValue1);
  Serial.print(" ");
  Serial.print(flexValue2);
  Serial.print(" ");
  Serial.print(flexValue3); 
  Serial.print(" ");
  Serial.print(flexValue4);
  Serial.print(" ");
  Serial.println(flexValue5);

//  delay(1000);
}

#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

const char* ssid = "mid";
const char* password = "onerupee";

ESP8266WebServer server(80);

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());

  server.on("/send", HTTP_POST, handleData);
  server.begin();
}

void loop() {
  server.handleClient();
 
}

void handleData() {
  String receivedData = server.arg("plain"); 
  Serial.println(receivedData);


  
  server.send(200, "text/plain", "Data received successfully");
}

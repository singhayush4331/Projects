#if defined(ESP32)
#include <WiFi.h>
#include <FirebaseESP32.h>
#elif defined(ESP8266)
#include <ESP8266WiFi.h>
#include <FirebaseESP8266.h>
#endif

//Provide the token generation process info.
#include <addons/TokenHelper.h>

//Provide the RTDB payload printing info and other helper functions.
#include <addons/RTDBHelper.h>

#define WIFI_SSID "no device found....."
#define WIFI_PASSWORD "tumkopatanahi?"

#define API_KEY "AIzaSyDCVkvRgJ_n8Gh_v0ewUJ0hdno91RBX12o"

#define DATABASE_URL "diy-room-a67f7-default-rtdb.asia-southeast1.firebasedatabase.app" //<databaseName>.firebaseio.com or <databaseName>.<region>.firebasedatabase.app

#define USER_EMAIL "room@firebase.com"
#define USER_PASSWORD "nachoo"

FirebaseData fbdo;

FirebaseAuth auth;
FirebaseConfig config;


int s1P = 13;
int s2P = 14;
int s3P = 18;
int s4P = 19;
int iSP = 2;

int r1 = 15;
int r2 = 4;
int r3 = 5;
int r4 = 23;

int s1, s2, s3, s4, fbr1, fbr2, fbr3, fbr4;
int a = 0, b = 0, c = 0 , d = 0, x = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to Wi-Fi");



  pinMode(s1P, INPUT);
  pinMode(s2P, INPUT);
  pinMode(s3P, INPUT);
  pinMode(s4P, INPUT);

  pinMode(r1, OUTPUT);
  pinMode(r2, OUTPUT);
  pinMode(r3, OUTPUT);
  pinMode(r4, OUTPUT);
  Serial.println("sdsddkjaj");
}

void loop() {
  // put your main code here, to run repeatedly:
  s1 = digitalRead(s1P);
  s2 = digitalRead(s2P);
  s3 = digitalRead(s3P);
  s4 = digitalRead(s4P);
  
  if(Firebase.get(fbdo,"/relay1")){
    fbr1 = fbdo.intData();
    Serial.print("fbr1: ");
    Serial.println(Firebase.getInt(fbdo, "/relay1"));
  }
  while (WiFi.status() != WL_CONNECTED){
    s1 = digitalRead(s1P);
    s2 = digitalRead(s2P);
    s3 = digitalRead(s3P);
    s4 = digitalRead(s4P);
    without_net();
    
  }
  if(x == 0){
    configCredentials();    
    x = 1;
  }
  
  with_net();
}

void with_net(){
  Serial.println("Connected");
  if(s1 == HIGH && a == 0){
    a = 1;
    Firebase.setInt(fbdo, "/relay1", a);
    Serial.print("r1 : ");
    Serial.println("HIGH");
    
  }
  else if(s1 == LOW && a == 1){
    a = 0;
    Firebase.setInt(fbdo, "/relay1", a);
  }
  
  if(s2 == HIGH && b == 0){
    b = 1;
    
    Firebase.setInt(fbdo, "/relay2", b);
    Serial.print("r2 : ");
    Serial.println("HIGH");
  
  }
  else if(s2 == LOW && b == 1){
    b = 0;
    Firebase.setInt(fbdo, "/relay2", b);
  }
  
  if(s3 == HIGH && c == 0){
    c = 1;
    Firebase.setInt(fbdo, "/relay3", c);
    Serial.print("r3 : ");
    Serial.println("HIGH");
  }
  else if(s3 == LOW && c == 1){
    c = 0;
    Firebase.setInt(fbdo, "/relay3", c);
    Serial.print("r3 : ");
    Serial.println("LOW");
  }
  
  if(s4 == HIGH && d == 0){
    d = 1;
    Firebase.setInt(fbdo, "/relay4", d);
    Serial.print("r4 : ");
    Serial.println("HIGH");
  }
  else if(s4 == LOW && d == 1){
    d = 0;
    Firebase.setInt(fbdo, "/relay4", d);
    Serial.print("r4 : ");
    Serial.println("LOW");
  }

  
  if(Firebase.get(fbdo,"/relay1")){
    if(fbdo.dataType() == "int"){
      fbr1 = fbdo.intData();
      if(fbr1 == 1){
        digitalWrite(r1, HIGH);
      }
      else if(fbr1 == 0){
        digitalWrite(r1, LOW);
      }
  }
  }
  if(Firebase.get(fbdo,"/relay2")){
    if(fbdo.dataType() == "int"){
      fbr2 = fbdo.intData();
      if(fbr2 == 1){
        digitalWrite(r2, HIGH);
      }
      else if(fbr2 == 0){
        digitalWrite(r2, LOW);
      }
  }
  }
  
  if(Firebase.get(fbdo,"/relay3")){
    if(fbdo.dataType() == "int"){
      fbr3 = fbdo.intData();
      if(fbr3 == 1){
        digitalWrite(r3, HIGH);
      }
      else if(fbr3 == 0){
        digitalWrite(r3, LOW);
      }
  }
  }
  
  if(Firebase.get(fbdo,"/relay4")){
    if(fbdo.dataType() == "int"){
      fbr4 = fbdo.intData();
      if(fbr4 == 1){
        digitalWrite(r4, HIGH);
      }
      else if(fbr4 == 0){
        digitalWrite(r4, LOW);
      }
  }
  }
  
  
}


void without_net(){
  Serial.println("Not connected");
  Serial.println(s1);
  Serial.println(s2);
  Serial.println(s3);
  Serial.println(s4);
  if(s1 == HIGH && a == 0){
    digitalWrite(r1, HIGH);
    a = 1;
  
    Serial.print("r1 : ");
    Serial.println("HIGH");
    
  }
  else if(s1 == LOW && a == 1){
    digitalWrite(r1, LOW);
    a = 0;
  }
  if(s2 == HIGH && b == 0){
    digitalWrite(r2, HIGH);
    b = 1;
    
    Serial.print("r2 : ");
    Serial.println("HIGH");
  
  }
  else if(s2 == LOW && b == 1){
    digitalWrite(r2, LOW);
    b = 0;
  }
  if(s3 == HIGH && c == 0){
    digitalWrite(r3, HIGH);
    c = 1;
    Serial.print("r3 : ");
    Serial.println("HIGH");
  }
  else if(s3 == LOW && c == 1){
    digitalWrite(r3, LOW);
    c = 0;
    Serial.print("r3 : ");
    Serial.println("LOW");
  }
  if(s4 == HIGH && d == 0){
    digitalWrite(r4, HIGH);
    d = 1;
    Serial.print("r4 : ");
    Serial.println("HIGH");
  }
  else if(s4 == LOW && d == 1){
    digitalWrite(r4, LOW);
    d = 0;
    Serial.print("r4 : ");
    Serial.println("LOW");
  }
}

void configCredentials(){
    Serial.println();
  Serial.print("Connected with IP: ");
  Serial.println(WiFi.localIP());
  Serial.println();

  Serial.printf("Firebase Client v%s\n\n", FIREBASE_CLIENT_VERSION);
  /* Assign the api key (required) */
  config.api_key = API_KEY;

  auth.user.email = USER_EMAIL;
  auth.user.password = USER_PASSWORD;

  config.database_url = DATABASE_URL;
  config.token_status_callback = tokenStatusCallback; //see addons/TokenHelper.h

  Firebase.begin(&config, &auth);

  //Comment or pass false value when WiFi reconnection will control by your code or third party library
  Firebase.reconnectWiFi(true);
}

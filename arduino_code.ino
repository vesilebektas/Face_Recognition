void setup() {
  pinMode(10, OUTPUT); // Yeşil ışık
  pinMode(9, OUTPUT); // Kırmızı ışık
  Serial.begin(9600);
  
  digitalWrite(10, HIGH);
  digitalWrite(9, HIGH);
  delay(1000);
  digitalWrite(10, LOW);
  digitalWrite(9, LOW);
}

void loop() {
  if (Serial.available() > 0) {
    char state = Serial.read();
    Serial.println(state);
    
    if (state == '1') {
      digitalWrite(10, HIGH);  // Yeşil ışık açık
      digitalWrite(9, LOW);   // Kırmızı ışık kapalı
    } 
    else if (state == '0') {
      digitalWrite(10, LOW);   // Yeşil ışık kapalı
      digitalWrite(9, HIGH);   // Kırmızı ışık açık
    }
    else if (state == '2') {
      digitalWrite(10, LOW);   // Yeşil ışık kapalı
      digitalWrite(9, LOW);    // Kırmızı ışık kapalı
    }
  }
}

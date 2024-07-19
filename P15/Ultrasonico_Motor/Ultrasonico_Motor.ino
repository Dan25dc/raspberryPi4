const int EchoPin = 8;    // Pin para la detección del eco
const int TriggerPin = 9; // Pin para producir el sonido ultrasónico

// Conexiones del driver L293D para un motor DC
int enA = 3;
int in1 = 6;
int in2 = 7;

void setup() {
  Serial.begin(9600);
  pinMode(TriggerPin, OUTPUT);
  pinMode(EchoPin, INPUT);
  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
}

void loop() {
  long duration, cm;

  // Realiza la medición de distancia
  cm = measureDistance();
  Serial.print(cm);
  Serial.print(",");

  if (cm > 5.0) {
    startMotor();
    Serial.println("Llenando ...");
  } else if (cm < 5.0) {
    stopMotor();
    Serial.println("Apagado - Tanque lleno ...");
  }
  delay(3000);
}

long microsecondsToCentimeters(long microseconds) {
  // 340 m/s 29 us/cm
  return microseconds / 29 / 2;
}

void startMotor() {
  analogWrite(enA, 255);
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
}

void stopMotor() {
  analogWrite(enA, 0);
}

long measureDistance() {
  digitalWrite(TriggerPin, LOW);
  delayMicroseconds(4);
  digitalWrite(TriggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(TriggerPin, LOW);
 
  return microsecondsToCentimeters(pulseIn(EchoPin, HIGH));
}
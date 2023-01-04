const int motor_A1 = 5;
const int motor_A2 = 6;
const int motor_B1 = 9;
const int motor_B2 = 10;
const int IR_R = A1;
const int IR_M = A3;
const int IR_L = A5;
int IR_L_data;
int IR_M_data;
int IR_R_data;
const int initial_speed = 250;
int speed;
char ch;

void setup() {
  pinMode(motor_A1, OUTPUT);
  pinMode(motor_A2, OUTPUT);
  pinMode(motor_B1, OUTPUT);
  pinMode(motor_B2, OUTPUT);
  pinMode(IR_L, INPUT);
  pinMode(IR_M, INPUT);
  pinMode(IR_R, INPUT);
  Serial.begin(9600);
  Serial.println("Success");
  speed = initial_speed;
}


void loop() {
  //IR 센서 값을 읽어 출력해주는 코드
  IR_L_data = digitalRead(IR_L);
  IR_M_data = digitalRead(IR_M);
  IR_R_data = digitalRead(IR_R);
  Serial.print(IR_L_data);
  Serial.print("-");
  Serial.print(IR_M_data);
  Serial.print("-");
  Serial.println(IR_R_data);

  line_tracer();

  // 객체 탐지 결과 시리얼 통신으로 받기
  if (Serial.available()) {
    ch = Serial.read();
  }
  // STOP
  if (ch == '0') {
    speed = 0;
  }
  // PERSON
  else if (ch == '1') {
    speed = 0;
  }
  // NONE
  else if (ch == '2') {
    speed = 250;
  }
}



void line_tracer() {
  // 2IR sensor
  if (IR_L_data == 0 and IR_R_data == 0) {
    Serial.println("직진");
    forward();
  }
  else if (IR_L_data == 1 and IR_R_data == 0) {
    Serial.println("좌회전 ");
    left();
  }
  else if (IR_L_data == 0 and IR_R_data == 1) {
    Serial.println("우회전");
    right();
  }
  else if (IR_L_data == 1 and IR_R_data == 1) {
    Serial.println("정지");
    stop();
  }
}

void right () {
  //우
  analogWrite(motor_A1, speed);
  analogWrite(motor_A2, 0);
  analogWrite(motor_B1, 0);
  analogWrite(motor_B2, 0);
}

void left() {
  //좌
  analogWrite(motor_A1, 0);
  analogWrite(motor_A2, 0);
  analogWrite(motor_B1, speed);
  analogWrite(motor_B2, 0);
}

void forward() {
  //전진
  analogWrite(motor_A1, speed);
  analogWrite(motor_A2, 0);
  analogWrite(motor_B1, speed);
  analogWrite(motor_B2, 0);
}

void backward() {
  //후진
  analogWrite(motor_A1, 0);
  analogWrite(motor_A2, speed);
  analogWrite(motor_B1, 0);
  analogWrite(motor_B2, speed);
}

void stop() {
  analogWrite(motor_A1, 0);
  analogWrite(motor_A2, 0);
  analogWrite(motor_B1, 0);
  analogWrite(motor_B2, 0);
}
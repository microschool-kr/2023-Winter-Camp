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
int speed = 250;
int slow_speed = 250 / 3;
char ch;
int cnt;
int i;

void setup() {
  pinMode(motor_A1, OUTPUT);
  pinMode(motor_A2, OUTPUT);
  pinMode(motor_B1, OUTPUT);
  pinMode(motor_B2, OUTPUT);
  pinMode(IR_L, INPUT);
  pinMode(IR_M, INPUT);
  pinMode(IR_R, INPUT);
  Serial.begin(9600);
  Serial.println("Start");
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
  
  // 객체 탐지 결과 시리얼 통신으로 받기
  cnt = Serial.available();
  if (cnt) { 
    for (i = 0; i < cnt; i++) {
      ch = Serial.read();
    }
  }
  
  // STOP
  if (ch == '0') {
    stop();
  }
  // PERSON
  else if (ch == '1') {
    stop();
  }
  // NONE
  else if (ch == '2') {
    if (IR_L_data == 0 and IR_M_data == 1 and IR_R_data == 0) {
      forward();
      Serial.print("forward");
    }
    else if (IR_L_data == 1 and IR_M_data == 1 and IR_R_data == 0) {
      left_soft();
      Serial.print("left_soft");
    }
    else if (IR_L_data == 1 and IR_M_data == 0 and IR_R_data == 0) {
      left();
      Serial.print("left");
    }
    else if (IR_L_data == 0 and IR_M_data == 1 and IR_R_data == 1) {
      right();
      Serial.print("right_soft");
    }
    else if (IR_L_data == 0 and IR_M_data == 0 and IR_R_data == 1) {
      right();
      Serial.print("right");
    }
    else if (IR_L_data == 1 and IR_M_data == 1 and IR_R_data == 1) {
      stop();
      Serial.print("stop");
    }    
  }
}

void forward() {
  //전진
  motor_con(speed, speed);
}
void left_soft() {
  //왼쪽
  motor_con(slow_speed, speed);
}
void left() {
  //왼쪽
  motor_con(0, speed);
}
void right() {
  //오른쪽
  motor_con(speed, 0);
}
void right_soft() {
  //오른쪽
  motor_con(speed, slow_speed);
}
void backward() {
  //후진
  motor_con(-speed, -speed);
}
void stop() {
  //정지
  motor_con(0, 0);
}

void motor_con(int pwmA, int pwmB) {
  // MOTOR A direction
  if (pwmA > 0) {
    analogWrite(motor_A1, abs(pwmA));
    analogWrite(motor_A2, LOW);
  } else if (pwmA < 0) {
    analogWrite(motor_A1, LOW);
    analogWrite(motor_A2, abs(pwmA));
  } else {
    digitalWrite(motor_A1, LOW);
    digitalWrite(motor_A2, LOW);
  }
  // MOTOR B direction
  if (pwmB > 0) {
    analogWrite(motor_B1, abs(pwmB));
    analogWrite(motor_B2, LOW);
  } else if (pwmB < 0) {
    analogWrite(motor_B1, LOW);
    analogWrite(motor_B2, abs(pwmB));
  } else {
    digitalWrite(motor_B1, LOW);
    digitalWrite(motor_B2, LOW);
  }
}


// Arduino sketch to track wheel revolutions on an exercise bike
// Bare-bones coe required to output number of revolutions via serial 
// Further processing to be carried out using Python on a raspberry pi connected via USB

const int  buttonPin = 2; 
int rotationCounter = 0;   
int currentState = 0;         
int lastState = 0;     

void setup() {
  pinMode(buttonPin, INPUT);
  Serial.begin(9600);
}


void loop() {
  currentState = digitalRead(buttonPin); // always 0 or 1

  // compare the buttonState to its previous state
  if (currentState != lastState) {
    // if the state has changed, increment the counter
    if (currentState == HIGH) {
      // if the current state is HIGH (1) then the wheel has made a rotation
      rotationCounter++;
      Serial.println(rotationCounter);
    } 
    // Delay a little bit to avoid bouncing
    delay(50);
  }
  // save the current state as the last state,
  //for next time through the loop
  lastState = currentState;


}
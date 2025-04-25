#include <Arduino.h>
#include "temp_sensor.h"

void setup() {
    Serial.begin(9600);
    initTempSensor();
}

void loop() {
    float value = readTempLevel();
    Serial.println(value);
    delay(1000);
}
#include <Arduino.h>
#include "temp_sensor.h"
#include "pump_motor.h"

enum actions
{
    FAST_PUMP,
    SLOW_PUMP
};

void setup()
{
    Serial.begin(9600);
    initTempSensor();
    initPumpMotor();
}

void loop()
{
    float value = readTempLevel();
    Serial.println(value);
    delay(1000);

    if (Serial.available())
    {
        int command = Serial.read();
        int arg = Serial.read();

        switch (command)
        {
        case (FAST_PUMP):
            fastMove(arg);
            break;
        case (SLOW_PUMP):
            slowMove(arg);
            break;
        default:
            Serial.println("ERROR: receieved " + command);
        }
    }
}
#include <Arduino.h>
#include <String.h>
#include "temp_sensor.h"
#include "pump_motor.h"

void setup()
{
    Serial.begin(9600);
    initTempSensor();
    initPumpMotor();
}

void loop()
{
    // float value = readTempLevel();
    // Serial.println(value);
    // delay(1000);

    if (Serial.available())
    {
        String command = Serial.readStringUntil('\n');
        int arg = (command.substring(8)).toInt();
        command = command.substring(0, 8);

        if (command.equals("fastpump"))
        {
            fastMove(arg);
        }
        else if (command.equals("slowpump"))
        {
            slowMove(arg);
        }
        else
        {
            Serial.println("ERROR: receieved " + command);
        }
    }
}
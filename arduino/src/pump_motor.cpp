#include <Arduino.h>
#include "pump_motor.h"
#include <TinyStepper_28BYJ_48.h>

const int MOTOR_IN1_PIN = 2;
const int MOTOR_IN2_PIN = 3;
const int MOTOR_IN3_PIN = 4;
const int MOTOR_IN4_PIN = 5;

const int STEPS_PER_REVOLUTION = 2048;

const int FAST_STEPS_PER_SECOND = 2048;
const int SLOW_STEPS_PER_SECOND = 128;

const int ACCEL_STEPS_PER_SECOND_PER_SECOND = 512;

const int FAST_STEPS = 2048;
const int SLOW_STEPS = 2048;

TinyStepper_28BYJ_48 pump;

void initPumpMotor()
{
    //
    // connect and configure the stepper motor to its IO pins
    //
    pump.connectToPins(MOTOR_IN1_PIN, MOTOR_IN2_PIN, MOTOR_IN3_PIN, MOTOR_IN4_PIN);
}

void slowMove(int timeInMillis)
{
    pump.setAccelerationInStepsPerSecondPerSecond(ACCEL_STEPS_PER_SECOND_PER_SECOND);
    pump.setSpeedInStepsPerSecond(SLOW_STEPS_PER_SECOND);
    pump.moveRelativeInSteps((timeInMillis / 1000) * SLOW_STEPS_PER_SECOND);
    delay(timeInMillis);
}

void fastMove(int timeInMillis)
{
    pump.setAccelerationInStepsPerSecondPerSecond(ACCEL_STEPS_PER_SECOND_PER_SECOND);
    pump.setSpeedInStepsPerSecond(FAST_STEPS_PER_SECOND);
    pump.moveRelativeInSteps((timeInMillis / 1000) * FAST_STEPS_PER_SECOND);
    delay(timeInMillis);
}
#include <Arduino.h>
#include "temp_sensor.h"
#include <DHT.h>
#define DHTTYPE     DHT11
#define DHT11_PIN   13

DHT dht(DHT11_PIN, DHTTYPE);

void initTempSensor() {
    dht.begin();
}

float readTempLevel() {
    return dht.readTemperature();
}
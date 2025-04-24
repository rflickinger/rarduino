# Rarduino Project

Ryan's attempt at the Garduino project, with only basic sensor implementation

## General Overview
The main components of the project will be:

On the pi:
- Python
    - Flask: to run the Rest API for taking actions over http
    - Pyserial: For communicating with the Raspberry pi over UART
- Postgres: For storing the collected data in a database

On the Arduino(s):
- The language will be cpp just due to running on an arduino
- Possibly two arduinos, one for sensors and one for controlling motors/pumps/etc.

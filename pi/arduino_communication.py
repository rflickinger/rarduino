import serial
import time

# Adjust the port if needed (e.g., /dev/ttyUSB0 if using USB-serial)
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

reads = 0

ser.flushInput()
while True:
    line = ser.readline().decode('utf-8').strip()
    if line:
        reads += 1
        print(f"Reads: {reads}\nReceived: {line}")
    time.sleep(1);
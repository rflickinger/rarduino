import serial

# Adjust the port if needed (e.g., /dev/ttyUSB0 if using USB-serial)
ser = serial.Serial('/dev/serial0', 9600, timeout=1)

while True:
    line = ser.readline().decode('utf-8').strip()
    if line:
        print(f"Received: {line}")
        # Next step: parse and store in your DB
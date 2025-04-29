import serial

def read_temp_from_serial(port='/dev/ttyUSB0', baudrate=9600):
    ser = serial.Serial(port, baudrate, timeout=1)
    line = ser.readline().decode('utf-8').strip()
    if line:
        try:
            return float(line)
        except ValueError:
            return None
import serial
import threading
from database import insert_sensor_data
from config import SERIAL_PORT, SERIAL_BAUD

def serial_reader():
    ser = serial.Serial(SERIAL_PORT, SERIAL_BAUD, timeout=1)
    while True:
        line = ser.readline().decode().strip()
        if line:
            try:
                sensor_type, value = line.split(':')
                insert_sensor_data(sensor_type, float(value))
                print(f"Ingested: {sensor_type} = {value}")
            except Exception as e:
                print("Malformed data or DB error:", e)

def start_ingestion_thread():
    thread = threading.Thread(target=serial_reader, daemon=True)
    thread.start()
import serial
from config import SERIAL_PORT, SERIAL_BAUD

def run_pump(board_id):
    with serial.Serial(SERIAL_PORT, SERIAL_BAUD, timeout=1) as ser:
        command = f"PUMP:{pump_id}\n"
        ser.write(command.encode())
        print(f"Sent: {command.strip()}")
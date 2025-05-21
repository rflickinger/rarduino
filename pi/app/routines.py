from database import get_latest_sensor_data

MOISTURE_THRESHOLD = 30.0

# def check_and_run_routines():
#     data = get_latest_sensor_data('moisture')
#     if data and data['value'] < MOISTURE_THRESHOLD:
#         run_pump(1)
#         return f"Moisture low ({data['value']}), pump triggered"
#     return f"Moisture OK ({data['value']}), no action"
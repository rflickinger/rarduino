from flask import Blueprint, jsonify, request
import json
from .database import db
from .models import Plant, Arduino
# from .routines import check_and_run_routines
 
garden_api = Blueprint('garden_api', __name__)

@garden_api.route("/")
def index():
    return jsonify({"message": "Welcome to the Smart Garden API"}), 200

# Get all plants
@garden_api.route("/plants", methods=["GET"])
def get_plants():
    plants = Plant.query.all()
    return jsonify([{
        "id": str(p.id),
        "plant_name": p.plant_name,
        "plant_type": p.plant_type,
        "enabled": p.enabled,
        "arduino_id": str(p.arduino_id) if p.arduino_id else None
    } for p in plants]), 200

# Add a new plant
@garden_api.route("/plants", methods=["POST"])
def create_plant():
    data = request.get_json()
    plant = Plant(
        plant_name=data["plant_name"],
        plant_type=data["plant_type"],
        enabled=data.get("enabled", True),
        arduino_id=data.get("arduino_id")
    )
    db.session.add(plant)
    db.session.commit()
    return jsonify({"message": "Plant added", "id": str(plant.id)}), 201

# Example: Get all Arduinos
@garden_api.route("/arduinos", methods=["GET"])
def get_arduinos():
    arduinos = Arduino.query.all()
    return jsonify([{
        "id": str(a.id),
        "serial_port": a.serial_port,
        "is_environment_tracker": a.is_environment_tracker
    } for a in arduinos]), 200

# @garden_api.route('/api/pump', methods=['POST'])
# def trigger_pump(pump_command_json):
#     """
#     Trigger a pump to run, receives json
#     ---
#     post:
#         description: Reads board_id, speed, and time from the passed in json
#         requestBody:
#             description: pump control request
#             content:
#                 application/json
#         responses:
#             200:
#                 description: pump control worked
#                 content:
#                     application/json
#             400:
#                 description: poorly formatted json
#                     content:
#                         application/json
#             406:
#                 description: Invalid board selected
#                     content:
#                         application/json
#     """
#     pump_command_dict = json.loads(pump_command_json)
#     board_id = pump_command_dict.get("board_uuid")
#     code, response = run_pump(board_id)
#     return json.dumps({ "status_code":code, "Response":response })

# @garden_api.route('/api/routines', methods=['POST'])
# def trigger_routines():
#     result = check_and_run_routines()
#     return jsonify({"status": "Routine executed", "result": result})
from flask import Blueprint, jsonify, request
from .database import db
from .models import Plant, Arduino
from .schemas import PlantSchema, ArduinoSchema

garden_api = Blueprint('garden_api', __name__)

@garden_api.route("/")
def index():
    """
    Root endpoint of the Rarduino API.
    ---
    responses:
      200:
        description: A welcome string
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: Welcome to the Rarduino API
    """
    return jsonify({"message": "Welcome to the Rarduino API"}), 200

@garden_api.route("/plants", methods=["GET"])
def get_plants():
    """
    Get all plants in the database.
    ---
    responses:
      200:
        description: A list of plants
        content:
          application/json:
            schema:
              type: array
              items:
                $ref: '#/components/schemas/PlantSchema'
    """
    plants = Plant.query.all()
    return PlantSchema(many=True).dump(plants), 200

@garden_api.route("/create_plant", methods=["POST"])
def create_plant():
    """
    Create a new plant entry.
    ---
    requestBody:
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/PlantSchema'
    responses:
      201:
        description: Plant successfully created
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: Plant added
                id:
                  type: string
    """
    schema = PlantSchema()
    data = schema.load(request.get_json())
    plant = Plant(**data)
    db.session.add(plant)
    db.session.commit()
    return jsonify({"message": "Plant added", "id": str(plant.id)}), 201

@garden_api.route("/arduinos", methods=["GET"])
def get_arduinos():
    """
    Get all Arduino devices.
    ---
    responses:
      200:
        description: A list of Arduinos
        content:
          application/json:
            schema:
              type: array
              items:
                $ref: '#/components/schemas/ArduinoSchema'
    """
    arduinos = Arduino.query.all()
    return ArduinoSchema(many=True).dump(arduinos), 200

@garden_api.route("/create_arduino", methods=["POST"])
def create_arduino():
    """
    Create a new Arduino entry.
    ---
    requestBody:
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ArduinoSchema'
    responses:
      201:
        description: Arduino successfully created
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: Plant added
                id:
                  type: string
    """
    schema = ArduinoSchema()
    data = schema.load(request.get_json())
    arduino = Arduino(**data)
    db.session.add(arduino)
    db.session.commit()
    return jsonify({"message": "Plant added", "id": str(arduino.id)}), 201
from marshmallow import Schema, fields

class PlantSchema(Schema):
    id = fields.String(dump_only=True)
    plant_name = fields.String(required=True)
    plant_type = fields.String(required=True)
    enabled = fields.Boolean(load_default=True)
    arduino_id = fields.String(allow_none=True)

class ArduinoSchema(Schema):
    id = fields.String(dump_only=True)
    serial_port = fields.String(required=True)
    is_environment_tracker = fields.Boolean(required=True)
    soil_temp_pin = fields.Integer()
    soil_moisture_pin = fields.Integer()
    pump_control_pin = fields.Integer()

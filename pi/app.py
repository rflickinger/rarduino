from flask import Flask, jsonify, render_template
from control import run_pump
import json
from routines import check_and_run_routines

app = Flask(__name__)
 
@app.route('/api/pump', methods=['POST'])
def trigger_pump(pump_command_json):
    """
    Trigger a pump to run, receives json
    ---
    post:
        description: Reads board_id, speed, and time from the passed in json
        requestBody:
            description: pump control request
            content:
                application/json
        responses:
            200:
                description: pump control worked
                content:
                    application/json
            400:
                description: poorly formatted json
                    content:
                        application/json
            406:
                description: Invalid board selected
                    content:
                        application/json
    """
    pump_command_dict = json.loads(pump_command_json)
    board_id = pump_command_dict.get("board_uuid")
    code, response = run_pump(board_id)
    return json.dumps({ "status_code":code, "Response":response })

    

# @app.route('/api/routines', methods=['POST'])
# def trigger_routines():
#     result = check_and_run_routines()
#     return jsonify({"status": "Routine executed", "result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
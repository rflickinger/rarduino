from flask import Flask, jsonify, render_template
from control import run_pump
from routines import check_and_run_routines

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/pump/<int:pump_id>', methods=['POST'])
def trigger_pump(pump_id):
    run_pump(pump_id)
    return jsonify({"status": "Pump triggered", "pump_id": pump_id})

@app.route('/api/routines', methods=['POST'])
def trigger_routines():
    result = check_and_run_routines()
    return jsonify({"status": "Routine executed", "result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
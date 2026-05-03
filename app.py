from flask import Flask, request, jsonify
from database import init_db, insert_data

app = Flask(__name__)

# ─── Receive data from ESP32 ──────────────────────────────────
@app.route('/data', methods=['POST'])
def receive_data():

    # Check if request has JSON body
    if not request.is_json:
        return jsonify({"status": "error", "message": "Request must be JSON"}), 400

    data = request.get_json()

    # Validate all required fields exist
    required_fields = ['voltage', 'current', 'power']
    for field in required_fields:
        if field not in data:
            return jsonify({
                "status": "error",
                "message": f"Missing field: {field}"
            }), 400

    # Validate all values are numbers
    try:
        voltage = float(data['voltage'])
        current = float(data['current'])
        power   = float(data['power'])
    except (ValueError, TypeError):
        return jsonify({
            "status": "error",
            "message": "voltage, current, power must be numbers"
        }), 400

    # Save to database
    try:
        insert_data(voltage, current, power)
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Database error: {str(e)}"
        }), 500

    # Log to terminal
    print(f"[DATA RECEIVED] Voltage: {voltage:.2f}V | "
          f"Current: {current:.2f}A | Power: {power:.2f}W")

    return jsonify({"status": "success"}), 200


# ─── Optional: View all stored data in browser ────────────────
@app.route('/readings', methods=['GET'])
def get_readings():
    from database import fetch_all
    rows = fetch_all()
    results = [
        {"id": r[0], "timestamp": r[1],
         "voltage": r[2], "current": r[3], "power": r[4]}
        for r in rows
    ]
    return jsonify(results), 200


# ─── Run server ───────────────────────────────────────────────
if __name__ == '__main__':
    init_db()                        # Create DB/table on startup
    app.run(host='0.0.0.0',          # Accept connections from ESP32 on network
            port=5000,
            debug=True)

# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Cyber Lite SOC is running!"

@app.route('/log', methods=['POST'])
def receive_log():
    data = request.get_json()
    print(f"Received log: {data}")
    return jsonify({"status": "received"}), 200

if __name__ == '__main__':
    app.run()

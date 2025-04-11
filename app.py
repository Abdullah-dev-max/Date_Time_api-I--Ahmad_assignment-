from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_current_datetime():
    # Get the current date and time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Return a JSON response
    return jsonify({'datetime': current_time})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

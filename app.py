from flask import Flask, jsonify
from datetime import datetime
import json

app = Flask(__name__)

@app.route('/datetime', methods=['GET'])
def default_function():
    return get_current_datetime()
@app.route('/', methods=['GET'])
def get_current_datetime():
   
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    
    output = {
        "status": "OK",
        "message": "success",
        "datetime": current_datetime
    }

    
    return jsonify(output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

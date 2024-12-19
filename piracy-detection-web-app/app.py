from flask import Flask, render_template, request, jsonify
from detection.obfuscation import detect_obfuscated_keyword  # Updated function using fuzzywuzzy

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', result=None)

@app.route('/check_piracy', methods=['POST'])
def check_piracy():
    data = request.get_json()  # Parse incoming JSON data
    text = data.get('text')  # Extract text input from the request
    
    # Check for obfuscation using fuzzywuzzy (or any other logic you use)
    result = detect_obfuscated_keyword(text)  # Replace with your actual detection logic
    
    # Return result as JSON
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')
